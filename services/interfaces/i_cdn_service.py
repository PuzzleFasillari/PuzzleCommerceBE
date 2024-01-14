from abc import ABC, abstractmethod


class ICDNService(ABC):

    @abstractmethod
    async def upload_file(self, bucket_name, file_path, object_key, acl='private'):
        raise NotImplementedError
