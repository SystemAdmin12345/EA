local multi = {"One", "Two", "Three", "Five"}

local function check(input)
    for i = 1, #multi do
        if input == multi[i] then
            return (0)
        end
    end
    return (1)
end

print(check("One")