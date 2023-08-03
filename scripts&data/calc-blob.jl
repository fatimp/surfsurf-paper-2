using NPZ
using FileIO
using Images
using FFTW
import CorrelationFunctions.Map as M
import CorrelationFunctions.Utilities as U

struct FuckKernel <: U.AbstractKernel
end

const foo = [1 1 1; 1 -8 1; 1 1 1]

U.extract_edges(array :: AbstractArray, filter :: FuckKernel, topology :: U.AbstractTopology) =
    abs.(imfilter(array, centered(foo / 6), U.edge2pad(topology)))

for side in [500, 1000, 2000, 3000]
    data = load("field-$(side).pbm") .|> Gray |> BitArray;
    npzwrite("field-ss-$(side).npy",
             fftshift(M.surf2(data, false; periodic = true, filter = U.ConvKernel(7))) * side^2)
end
