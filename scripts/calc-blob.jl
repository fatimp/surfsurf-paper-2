using NPZ
using FileIO
using Images
using FFTW
import CorrelationFunctions.Map as M
import CorrelationFunctions.Utilities as U

flt = U.EdgeFilter(U.BCPeriodic(), U.Kernel3x3())
for side in 500:500:3000
    data = load("field-$(side).pbm") .|> Gray |> BitArray;
    npzwrite("field-ss-$(side).npy",
             fftshift(M.surfsurf(data, false; periodic = true, filter = flt)) * side^2)
end
