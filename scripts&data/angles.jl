import CorrelationFunctions.Utilities as U
using DelimitedFiles

f(x, y, ny, nx) = nx * x + ny * y

function f(α; n, method)
    x = range(-1, 1, length=n)
    A = [f(x, y, sincos(α)...) > 0 for x in x, y in x]
    An = U.extract_edges(A, method)

    B = [f(x, y, sincos(0)...) > 0 for x in x, y in x]
    Bn = U.extract_edges(B, method)

    return sum(An .* Bn)
end

ϵ = 0.1
αs = (0+ϵ):0.001:(π-ϵ)
approx = f.(αs; n = 400, method = U.EdgeFilter(U.BCReflect(), U.Kernel5x5()))
open("angles-5x5.dat", "w") do out
    writedlm(out, hcat(αs, approx))
end
