# Exercise 0.2 – Probability of Drawing Two Aces

This exercise is based on Exercise 0.2 from Chapter 0 of _The Nature of Code_ by Daniel Shiffman.

## Problem Statement

**Question:**  
What is the probability of drawing two aces in a row from a deck of 52 cards, if you reshuffle your first draw back into the deck before making your second draw? What would that probability be if you didn’t reshuffle after your first draw?

---

## Solution

### 1. With Reshuffling After the First Draw

- There are 52 cards in the deck, 4 of which are aces.
- The probability of drawing an ace on the first draw is **4/52**.
- After returning the card and reshuffling, the probability of drawing an ace again is still **4/52**.
- Since the two [events are independent](<https://en.wikipedia.org/wiki/Independence_(probability_theory)>), multiply the probabilities (those are also [multiple events](https://courses.lumenlearning.com/waymakercollegealgebra/chapter/probability-for-multiple-events/)):

  ```
  Probability = (4/52) × (4/52) = 16/2704 = 1/169 ≈ 0.59%
  ```

### 2. Without Reshuffling After the First Draw

- The probability of drawing an ace on the first draw is **4/52**.
- After removing one ace, there are now 3 aces left in a deck of 51 cards.
- The probability of drawing another ace is **3/51**.
- Multiply the probabilities:

  ```
  Probability = (4/52) × (3/51) = 12/2652 = 1/221 ≈ 0.45%
  ```

---

## Summary Table

| Scenario            | Probability Calculation | Result        |
| ------------------- | ----------------------- | ------------- |
| With reshuffling    | (4/52) × (4/52)         | 1/169 ≈ 0.59% |
| Without reshuffling | (4/52) × (3/51)         | 1/221 ≈ 0.45% |
