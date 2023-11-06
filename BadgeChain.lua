local Badges = 0
local MaxBadges = 42069


print("Welcome to badge chain!")

while Badges < MaxBadges do
    Badges = Badges + 1
    print("Badges: "..Badges.."/"..MaxBadges)
end