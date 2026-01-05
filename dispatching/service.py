from dispatching.models import Package, DispatchType


def sort(width: float, height: float, length: float, mass: int) -> str:
    package = Package(width, height, length, mass)
    match (package.is_bulky, package.is_heavy):
        case (True, True):
            return DispatchType.REJECTED.value
        case (True, False):
            return DispatchType.SPECIAL.value
        case (False, True):
            return DispatchType.SPECIAL.value
    return DispatchType.STANDARD.value
