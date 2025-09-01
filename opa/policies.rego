package microtask

default allow = false

# Allow service-1 to call service-2
allow {
    input.source == "service-1"
    input.destination == "service-2"
}

# You can extend to time-based policies later
