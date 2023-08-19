import connexion
import six

from swagger_server.models.cloud import Cloud  # noqa: E501
from swagger_server import util


def cancel_cloud_by_id(cloud_id):  # noqa: E501
    """method of deleting order in the cloud

     # noqa: E501

    :param cloud_id: order identification in cloud
    :type cloud_id: str

    :rtype: Cloud
    """
    return 'do some magic!'


def create_cloud():  # noqa: E501
    """method of creating order in the cloud

     # noqa: E501


    :rtype: Cloud
    """
    return 'do some magic!'


def get_all_clouds():  # noqa: E501
    """method of getting cloud resource

     # noqa: E501


    :rtype: Cloud
    """
    return 'do some magic!'


def get_order_by_id(cloud_id):  # noqa: E501
    """method of getting order

     # noqa: E501

    :param cloud_id: order identification in cloud
    :type cloud_id: str

    :rtype: Cloud
    """
    return 'do some magic!'
