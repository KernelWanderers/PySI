from core.managers.base import BaseManager
from core.hardware.storage import StorageDevice
from util.util import Util

class StorageManager(BaseManager[StorageDevice]):
    def __init__(self):
        pass
    
    def net_info(self) -> list[StorageDevice]:
        """
        Extracts information about the Storage device(s)
        inside of the current system.

        Automatically takes care of providing the
        appropriate method in context of the platform.
        """
        kernel = Util.get_kernel()

        # Unsupported platform or error.
        if kernel.get("name", "").lower() == "unknown":
            return []
        
        try:
            return getattr(self, "_" + kernel.get("short"))()
        except Exception:
            return []

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> list[StorageDevice] | None:
        raise NotImplementedError

    def _win(self) -> list[StorageDevice] | None:
        raise NotImplementedError
    
    def _linux(self) -> list[StorageDevice] | None:
        raise NotImplementedError