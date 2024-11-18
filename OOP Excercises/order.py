class OrderItem:
    """Order Item requested by a customer."""
    def __init__(self, customer: str, name: str, quantity: int, one_item_volume: int):
        """
        Order item constructor.
        :param customer: requester name.
        :param name: the name of the item.
        :param quantity: quantity that shows how many such items customer needs.
        :param one_item_volume: the volume of one item.
        """
        self.customer = customer
        self.name = name
        self.quantity = quantity
        self.one_item_volume = one_item_volume

    @property
    def total_volume(self) -> int:
        """
        Calculate and return total volume of all order items together.
        :return: Total volume (cm^3), int.
        """
        return self.quantity * self.one_item_volume


class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: list):
        """
        Order constructor.
        :param order_items: list of order items.
        """
        self.order_items = order_items
        self.destination = None

    @property
    def total_quantity(self) -> int:
        """
        Calculate and return the sum of quantities of all items in the order.
        :return: Total quantity as int.
        """
        total = 0
        for i in self.order_items:
            total += i.quantity
        return total

    @property
    def total_volume(self) -> int:
        """
        Calculate and return the total volume of all items in the order.
        :return: Total volume (cm^3) as int.
        """
        total = 0
        for i in self.order_items:
            total += i.total_volume
        return total


class Container:
    """Container to transport orders."""

    def __init__(self, volume: int, orders: list, destination: str = None):
        """
        Initialize container.
        :param volume: Container volume in cm^3
        :param orders: List of orders
        :param destination: Container destination (optional)
        """
        self.volume = volume
        self.orders = orders
        self.destination = destination

    @property
    def volume_left(self) -> int:
        """
        Calculate and returns the volume left in the container
        :return: Total volume left as int.
        """
        used_volume = 0
        for order in self.orders:
            used_volume += order.total_volume
        remaining_volume = self.volume - used_volume
        if remaining_volume < 0:
            return 0
        return remaining_volume

    def add_order(self, order: Order) -> bool:
        """
        Try to add an order to the container.
        :param order: Order to add
        :return: True if order was added, False if it wouldn't fit
        """
        if order.total_volume <= self.volume_left:
            self.orders.append(order)
            return True
        return False


class OrderAggregator:
    """Algorithm of aggregating orders."""
    def __init__(self):
        """Initialize order aggregator."""
        self.order_items = []

    def add_item(self, item: OrderItem):
        """
        Add order item to the aggregator.
        :param item: Item to add.
        :return: None
        """
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int):
        """
        Create an order for customer which contains order lines added by add_item method.
        Iterate over added orders items and add them to order if they are for given customer
        and can fit to the order.
        :param customer: Customer's name to create an order for.
        :param max_items_quantity: Maximum amount on items in order.
        :param max_volume: Maximum volume of order. All items volumes must not exceed this value.
        :return: Order.
        """
        items = []
        current_quantity = 0
        current_volume = 0

        for item in self.order_items:
            if item.customer == customer:
                if (current_quantity + item.quantity <= max_items_quantity and
                        current_volume + item.total_volume <= max_volume):
                    items.append(item)
                    current_quantity += item.quantity
                    current_volume += item.total_volume

        self.order_items = [item for item in self.order_items if item not in items]

        return Order(items)


class ContainerAggregator:
    """Algorithm to prepare containers."""
    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.
        :param container_volume: Volume of each container created by this aggregator.
        """
        self.container_volume = container_volume
        self.not_used_orders = []

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.
        If order cannot be put to a container, it is added to self.not_used_orders list.
        :param orders: tuple of orders.
        :return: dict where keys are destinations and values are containers to that destination with orders.
        """
        result = {}

        for order in orders:
            if not order.order_items or not hasattr(order, 'destination'):
                continue

            if order.total_volume > self.container_volume:
                self.not_used_orders.append(order)
                continue

            if order.destination not in result:
                result[order.destination] = []

            added = False
            for container in result[order.destination]:
                if container.add_order(order):
                    added = True
                    break

            if not added:
                new_container = Container(self.container_volume, [], order.destination)
                if new_container.add_order(order):
                    result[order.destination].append(new_container)
                else:
                    self.not_used_orders.append(order)

        return result