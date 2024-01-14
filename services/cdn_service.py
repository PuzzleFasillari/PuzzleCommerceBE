import logging

from services.interfaces.i_cdn_service import ICDNService

from aiobotocore.session import get_session
import botocore.config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CDNService(ICDNService):
    def __init__(self, endpoint_url, region_name, access_key_id, secret_access_key):
        self.endpoint_url = endpoint_url
        self.region_name = region_name
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    async def upload_file(self, bucket_name, file_data, object_key, acl='private'):
        session = get_session()
        async with session.create_client('s3',
                                         endpoint_url=self.endpoint_url,
                                         config=botocore.config.Config(s3={'addressing_style': 'virtual'}),
                                         region_name=self.region_name,
                                         aws_access_key_id=self.access_key_id,
                                         aws_secret_access_key=self.secret_access_key) as client:
            await client.put_object(Bucket=bucket_name,
                                    Key=object_key,
                                    Body=file_data,
                                    ACL=acl)
