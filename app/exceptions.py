class NoPicturesOnHosting(Exception):
    pass


class HostingCommunicationError(Exception):
    pass


class ItemObjectNotCreated(Exception):
    pass


class DatabaseConnectionError(Exception):
    pass


class DatabaseAddItemError(Exception):
    pass


class RequestError(Exception):
    pass


class RequestNotCorrectError(Exception):
    pass


class CannotGetEbayAccessToken(Exception):
    pass


class CannotCreateEbayInventoryItem(Exception):
    pass


class CannotCreateEbayOffer(Exception):
    pass


class CannotExchangeCurrency(Exception):
    pass


class CannotPublishEbayOffer(Exception):
    pass


class DatabaseGetItemsError(Exception):
    pass