module Torquatsky
using DelimitedFiles
using Images
using Interpolations
using QuadGK
import CorrelationFunctions.Map as M
import CorrelationFunctions.Utilities as U
export do_it!

struct FuckKernel <: U.AbstractKernel
end

const foo = [1 1 1; 1 -8 1; 1 1 1]

U.extract_edges(array :: AbstractArray, filter :: FuckKernel, topology :: U.AbstractTopology) =
    abs.(imfilter(array, centered(foo / 6), U.edge2pad(topology)))

function draw_ball(s, r)
    array = falses(s)
	center = @. (s ÷ 2) |> floor |> Int

    for idx in CartesianIndices(array)
        dist = sum((Tuple(idx) .- center) .^ 2)
        if dist <= r^2
            array[idx] = true
        end
    end

    return array
end

ss(x, R) = x < 2R ? 4R^2/(x * sqrt(4R^2 - x^2)) : 0

function calc_error(array, R, ε = 0.01)
    xs = range(0, 0.5, length(array))
    inter = linear_interpolation(xs, array)
    fn1(x) =  ss(x, R)^2
    fn2(x) = (ss(x, R) - inter(x))^2
    ntheory = quadgk(fn1, ε, 2R - ε)[1]
    ndiff = quadgk(fn2, ε, 2R - ε)[1]
    return sqrt(ndiff/ntheory)
end

function do_it!()
    R = 0.0334
    errors = Float64[]
    criteria = Float64[]

    for side in 100:100:3100
        disk = draw_ball((side, side), R*side)
        println(side)
        ss = M.surf2(disk, false; periodic = true, filter = U.ConvKernel(7)) |> M.average_directions
        push!(errors, calc_error(ss * side^2, R, 0.005))
        push!(criteria, U.lowfreq_energy_ratio(disk))
        open("disks-$(side)-we-ss.dat", "w") do out
            writedlm(out, ss)
        end
    end

    open("errors-7x7.dat", "w") do out
        writedlm(out, hcat(errors, criteria))
    end
end

end
