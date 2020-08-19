# Function with return
function sphere_vol(r)
    return 4/3*pi*r^3
end

# Function
quadratic(a, sqr_term, b) = (-b + sqr_term) / 2a

# Function with argument types
function quadratic2(a::Float64, b::Float64, c::Float64)
    sqr_term = sqrt(b^2-4a*c)
    r1 = quadratic(a, sqrt_term, b)
    r2 = quadratic(a, -sqrt_term, b)
    
    # The last term is return if return is omitted
    r1, r2
end

vol = sphere_vol(3)
# @printf
using Printf
@printf "volume = %0.3f\n" vol

quad1, quad2 = quadratic2(2.0, -2.0, -12.0)
println("Result 1: ", quad1)
println("Result 2: ", quad2)
