module Torquatsky
using DelimitedFiles
import CorrelationFunctions.Map as M
import CorrelationFunctions.Utilities as U
export do_it!

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
    flt = U.EdgeFilter(U.BCPeriodic(), U.Kernel3x3())
    for side in 100:100:3100
        disk = draw_ball((side, side), R*side)
        println(side)
        println(U.lowfreq_energy_ratio(disk))

        ss = M.surfsurf(disk, false; periodic = true, filter = flt) |> M.average_directions

        open("disks-$(side)-we-ss.dat", "w") do out
            writedlm(out, ss)
        end
    end
end

end
