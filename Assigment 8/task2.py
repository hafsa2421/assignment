import unittest
from typing import Union

def assign_grade(score: Union[int, float]) -> str:
    """Return grade for score: 90-100 A, 80-89 B, 70-79 C, 60-69 D, <60 F.
    Raises ValueError for non-numeric or out-of-range inputs.
    """
    if not isinstance(score, (int, float)):
        raise ValueError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    s = int(score)
    if 90 <= s <= 100:
        return "A"
    if 80 <= s <= 89:
        return "B"
    if 70 <= s <= 79:
        return "C"
    if 60 <= s <= 69:
        return "D"
    return "F"


class TestAssignGrade(unittest.TestCase):
    def test_boundary_values_A(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(100), "A")

    def test_boundary_values_B(self):
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(89), "B")

    def test_boundary_values_C(self):
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(79), "C")

    def test_boundary_values_D(self):
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(69), "D")

    def test_boundary_values_F(self):
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(0), "F")

    def test_float_scores(self):
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(59.99), "F")

    def test_invalid_negative(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)

    def test_invalid_over_100(self):
        with self.assertRaises(ValueError):
            assign_grade(105)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            assign_grade("eighty")


if __name__ == "__main__":
    import sys

    # Run unit tests if "test" passed, otherwise run interactive prompt
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        print("Interactive grade checker (enter 'q' to quit).")
        while True:
            s = input("Enter score (0-100): ").strip()
            if s.lower() == "q" or s == "":
                print("Exiting.")
                break
            try:
                # allow integer or float input
                val = float(s)
                grade = assign_grade(val)
                print(f"Score: {val} -> Grade: {grade}")
            except Exception as e:
                print("Invalid input:", e)
