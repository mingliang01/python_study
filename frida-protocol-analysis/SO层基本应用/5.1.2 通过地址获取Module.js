Process.findModuleByAddress(address);
Process.getModuleByAddress(address);

function findModuleByAddress(address: NativePointerValue): Module | null;
function getModuleByAddress(address: NativePointerValue): Module;

interface ObjectWrapper {
    handle: NativePointer;
}
type NativePointerValue = NativePointer | ObjectWrapper;