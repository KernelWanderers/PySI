from core.managers.base import BaseManager
from core.hardware.gpu import GPU
from util.util import Util

class GPUManager(BaseManager[GPU]):
    def __init__(self):
        pass

    def gpu_info(self) -> list[GPU]:
        """
        Extracts information about the GPU(s) inside
        of the current system.

        Automatically takes care of providing the
        appropriate method in context of the platform.
        """
        kernel = Util.get_kernel()

        # Unsupported platform or error.
        if kernel.get("name", "").lower() == "unknown":
            return []

        return getattr(self, "_" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> list[GPU]:
        raise NotImplementedError

    def _win(self) -> list[GPU]:
        raise NotImplementedError

    def _linux(self) -> list[GPU]:
        raise NotImplementedError
