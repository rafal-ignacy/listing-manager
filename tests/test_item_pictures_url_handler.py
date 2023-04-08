import pytest
import mock
import requests

from app.utils.item_pictures_url_handler import ItemPicturesUrlHandler
from app.exceptions import NoPicturesOnHosting, HostingCommunicationError


def test_get_urls_one_url():
    item_pictures_url_handler = ItemPicturesUrlHandler(1, "K")
    result = item_pictures_url_handler.get_urls()
    print(result)
    assert result == "https://taxidermypoland.com/listing-manager/1K-1.JPG"


def test_get_urls_multiple_urls():
    item_pictures_url_handler = ItemPicturesUrlHandler(2, "K")
    result = item_pictures_url_handler.get_urls()
    print(result)
    assert result == "https://taxidermypoland.com/listing-manager/2K-1.JPG;https://taxidermypoland.com/listing-manager/2K-2.JPG"


def test_get_urls_no_pictures_on_hosting():
    item_pictures_url_handler = ItemPicturesUrlHandler(3, "K")
    with pytest.raises(NoPicturesOnHosting):
        item_pictures_url_handler.get_urls()


def test_get_urls_hosting_communication_error():
    item_pictures_url_handler = ItemPicturesUrlHandler(2, "K")
    with mock.patch('requests.get', side_effect=requests.RequestException('Failed Request')):
        with pytest.raises(HostingCommunicationError):
            item_pictures_url_handler.get_urls()
