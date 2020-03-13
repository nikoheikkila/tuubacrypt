# TuubaCrypt 🎺

They say you should never write your own encryption algorithm. Sounds like _fun_. That's what we are going to do.

> "Tuuba" is Finnish and translates to ["Tuba"](https://en.wikipedia.org/wiki/Tuba) since this package is as useful to the software development as a random person sitting in your office playing tuba.

## Encrypting Data

Encryption works for letters `A-Z` and numbers `0-9`, and is case sensitive. Every other character in input data flows through unchanged. To be really ~~secure~~ silly, package translates letters and numbers wrapping at edges, e.g. `Z => A` and `9 => 0`.

First affected character is translated by **1** (`A => B` or `1 => 2`). Second affected character is translated by **2** (`O => Q` or `7 => 9`) until the end of the string.

## Decrypting Data

Decryption works in a similar manner by translating characters in different direction. For example, the fourth affected character in decryption is translated like `K => H` or `2 => 8`.

## License

Just walk away, OK?

![License](https://media.giphy.com/media/PjfpYh9oqpd0Q/giphy.gif)

## Thanks

**Mikko Vieru**, for the wacky idea.
