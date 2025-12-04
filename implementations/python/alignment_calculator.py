"""
Universal Alignment Theory - Python Implementation

Core alignment calculation module for measuring mutual information
between goals and system states.
"""

import numpy as np
from scipy import stats
from typing import List, Tuple, Union


class AlignmentCalculator:
      """
          Core calculator for Universal Alignment Theory metrics.
              """

    def __init__(self, alpha: float = 0.5):
              """
                      Initialize alignment calculator.

                                      Args:
                                                  alpha: Sensitivity parameter for threshold calculation
                                                          """
              self.alpha = alpha

    def mutual_information(self, goals: List[float], state: List[float]) -> float:
              """
                      Calculate mutual information between goals and system state.

                                      Args:
                                                  goals: Goal vector
                                                              state: Current system state vector

                                                                                  Returns:
                                                                                              Mutual information I(G;Z)
                                                                                                      """
              # Convert to numpy arrays
              g = np.array(goals)
              z = np.array(state)

        # Calculate joint and marginal entropies
              joint_entropy = self._joint_entropy(g, z)
              goal_entropy = self._entropy(g)
              state_entropy = self._entropy(z)

        # I(G;Z) = H(G) + H(Z) - H(G,Z)
              return goal_entropy + state_entropy - joint_entropy

    def alignment_threshold(self, n_states: int) -> float:
              """
                      Calculate minimum alignment threshold.

                                      Args:
                                                  n_states: Number of possible system states

                                                                      Returns:
                                                                                  Minimum threshold I_min
                                                                                          """
              return np.log2(n_states) * self.alpha

    def is_aligned(self, mutual_info: float, threshold: float) -> bool:
              """
                      Check if system is aligned based on threshold.

                                      Args:
                                                  mutual_info: Calculated mutual information
                                                              threshold: Alignment threshold

                                                                                  Returns:
                                                                                              True if aligned, False otherwise
                                                                                                      """
              return mutual_info >= threshold

    def _entropy(self, x: np.ndarray) -> float:
              """Calculate entropy of a vector."""
              # Normalize to probability distribution
              p = x / np.sum(x)
              # Remove zeros to avoid log(0)
              p = p[p > 0]
              return -np.sum(p * np.log2(p))

    def _joint_entropy(self, x: np.ndarray, y: np.ndarray) -> float:
              """Calculate joint entropy of two vectors."""
              # Create joint distribution
              joint = np.outer(x, y)
              joint = joint / np.sum(joint)
              # Remove zeros
              joint = joint[joint > 0]
              return -np.sum(joint * np.log2(joint))


# Example usage
if __name__ == "__main__":
      calc = AlignmentCalculator()

    # Example goals and state
      goals = [0.8, 0.6, 0.9]
      state = [0.7, 0.65, 0.85]

    # Calculate alignment
      alignment = calc.mutual_information(goals, state)
      threshold = calc.alignment_threshold(len(goals))

    print(f"Alignment score: {alignment:.3f}")
    print(f"Threshold: {threshold:.3f}")
    print(f"System aligned: {calc.is_aligned(alignment, threshold)}")
