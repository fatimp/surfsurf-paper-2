module Torquatsky
using DelimitedFiles
using Images
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

function do_it!()
    R = 0.0334
    for side in 100:100:3100
        disk = draw_ball((side, side), R*side)
        println(side)
        println(U.lowfreq_energy_ratio(disk))

        ss = M.surf2(disk, false; periodic = true, filter = U.ConvKernel(7)) |> M.average_directions

        open("disks-$(side)-we-ss.dat", "w") do out
            writedlm(out, ss)
        end
    end
end

end
