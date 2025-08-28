#!/usr/bin/env python3
"""
Advanced Math Question Generator - Professional Edition
Generates comprehensive, curriculum-aligned mathematics assessment questions
with detailed explanations, multiple solution methods, and rigorous validation.

Author: AI Assistant
Date: August 2025
Version: 2.0
License: MIT
"""

import random
import math
import json
import logging
from typing import List, Dict, Tuple, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import numpy as np
from fractions import Fraction
import sympy as sp
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DifficultyLevel(Enum):
    """Enumeration for question difficulty levels"""
    EASY = "easy"
    MODERATE = "moderate"
    HARD = "hard"

@dataclass
class CurriculumTopic:
    """Represents a curriculum topic with hierarchy"""
    subject: str
    unit: str
    topic: str

    def __str__(self):
        return f"{self.subject} → {self.unit} → {self.topic}"

@dataclass
class QuestionData:
    """Comprehensive data structure for a math question"""
    question: str
    instruction: str
    options: List[str]
    correct_answer_index: int
    explanation: str
    curriculum: CurriculumTopic
    difficulty: DifficultyLevel
    order: int = 1
    plus_marks: int = 1
    latex_expressions: List[str] = field(default_factory=list)
    solution_methods: List[str] = field(default_factory=list)
    common_mistakes: List[str] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        """Validate question data completeness and correctness"""
        if not self.question or not self.instruction:
            return False
        if len(self.options) < 2 or self.correct_answer_index >= len(self.options):
            return False
        if not self.explanation or len(self.explanation) < 50:
            return False
        return True

class MathQuestionGenerator:
    """
    Advanced mathematics question generator with comprehensive curriculum support
    and multiple solution methodologies
    """

    def __init__(self):
        """Initialize the generator with curriculum and configuration"""
        self.curriculum_hierarchy = self._load_curriculum_hierarchy()
        self.question_templates = self._initialize_question_templates()
        self.mathematical_constants = {
            'pi': math.pi,
            'e': math.e,
            'golden_ratio': (1 + math.sqrt(5)) / 2
        }
        logger.info("Math Question Generator initialized successfully")

    def _load_curriculum_hierarchy(self) -> Dict[str, Dict[str, List[str]]]:
        """Load the complete curriculum hierarchy as specified in requirements"""
        return {
            "Quantitative Math": {
                "Problem Solving": [
                    "Numbers and Operations", "Algebra", "Geometry",
                    "Problem Solving", "Probability and Statistics", "Data Analysis"
                ],
                "Algebra": [
                    "Algebraic Word Problems", "Interpreting Variables",
                    "Polynomial Expressions (FOIL/Factoring)", "Rational Expressions",
                    "Exponential Expressions (Product rule, negative exponents)",
                    "Quadratic Equations & Functions (Finding roots/solutions, graphing)",
                    "Functions Operations"
                ],
                "Geometry and Measurement": [
                    "Area & Volume", "Perimeter", "Lines, Angles, & Triangles",
                    "Right Triangles & Trigonometry", "Circles (Area, circumference)",
                    "Coordinate Geometry", "Slope", "Transformations (Dilating a shape)",
                    "Parallel & Perpendicular Lines", "Solid Figures (Volume of Cubes)"
                ],
                "Numbers and Operations": [
                    "Basic Number Theory", "Prime & Composite Numbers", "Rational Numbers",
                    "Order of Operations", "Estimation", "Fractions, Decimals, & Percents",
                    "Sequences & Series", "Computation with Whole Numbers", "Operations with Negatives"
                ],
                "Data Analysis & Probability": [
                    "Interpretation of Tables & Graphs", "Trends & Inferences",
                    "Probability (Basic, Compound Events)", "Mean, Median, Mode, & Range",
                    "Weighted Averages", "Counting & Arrangement Problems"
                ],
                "Reasoning": ["Word Problems"]
            }
        }

    def _initialize_question_templates(self) -> Dict[str, Dict]:
        """Initialize question templates with parameters and constraints"""
        return {
            "coordinate_geometry_parallelogram": {
                "base_difficulty": DifficultyLevel.MODERATE,
                "vertex_range": (-8, 8),
                "requires_area_calculation": True,
                "solution_methods": ["vector_addition", "diagonal_bisection", "area_verification"]
            },
            "complex_word_problem": {
                "base_difficulty": DifficultyLevel.HARD,
                "involves_percentages": True,
                "multi_step": True,
                "real_world_context": True,
                "solution_methods": ["algebraic_setup", "step_by_step", "verification"]
            },
            "algebraic_manipulation": {
                "base_difficulty": DifficultyLevel.MODERATE,
                "polynomial_degree": (1, 3),
                "includes_factoring": True,
                "solution_methods": ["algebraic_manipulation", "graphical_analysis"]
            }
        }

    def generate_coordinate_geometry_question(self,
                                            difficulty: DifficultyLevel = DifficultyLevel.MODERATE,
                                            include_area: bool = True) -> QuestionData:
        """
        Generate a comprehensive coordinate geometry question about parallelograms
        with multiple solution methods and detailed explanations
        """
        # Generate three vertices for a triangle
        vertices = self._generate_triangle_vertices()
        a, b, c = vertices

        # Calculate the fourth vertex for parallelogram using vector addition
        d = self._calculate_parallelogram_vertex(a, b, c)

        # Calculate area of the original triangle
        triangle_area = self._calculate_triangle_area(a, b, c)
        parallelogram_area = 2 * triangle_area  # Parallelogram area = 2 × triangle area

        # Generate plausible distractors
        distractors = self._generate_coordinate_distractors(d, 4)

        # Create options list
        options = [d] + distractors
        random.shuffle(options)
        correct_index = options.index(d)

        # Format options with area information
        formatted_options = [
            f"S{opt} and area = {parallelogram_area:.0f} square units"
            for opt in options
        ]

        # Generate comprehensive explanation
        explanation = self._generate_detailed_parallelogram_explanation(
            a, b, c, d, triangle_area, parallelogram_area
        )

        # Create question text
        question_text = (
            f"In the coordinate plane below, quadrilateral PQRS has three known vertices: "
            f"P{a}, Q{b}, and R{c}. Point S must be positioned such that PQRS forms a "
            f"parallelogram with diagonals intersecting at point M. Additionally, if the "
            f"area of triangle PQR is {triangle_area:.0f} square units, determine the "
            f"coordinates of point S and verify that the parallelogram PQRS has twice this area."
        )

        return QuestionData(
            question=question_text,
            instruction="Analyze the geometric relationships and use multiple methods to find point S. Show all algebraic work and verify your answer using at least two different approaches.",
            options=formatted_options,
            correct_answer_index=correct_index,
            explanation=explanation,
            curriculum=CurriculumTopic("Quantitative Math", "Geometry and Measurement", "Coordinate Geometry"),
            difficulty=difficulty,
            latex_expressions=[
                r"\overrightarrow{PQ} = \overrightarrow{SR}",
                r"\frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|"
            ],
            solution_methods=["Vector Addition Method", "Diagonal Bisection Method", "Area Verification"],
            common_mistakes=["Confusing vector direction", "Calculation errors in midpoint formula"],
            prerequisites=["Coordinate plane basics", "Vector operations", "Area calculations"]
        )

    def _generate_triangle_vertices(self) -> List[Tuple[int, int]]:
        """Generate three vertices that form a valid triangle"""
        while True:
            vertices = [
                (random.randint(-8, 8), random.randint(-8, 8))
                for _ in range(3)
            ]
            # Ensure vertices are not collinear
            if self._are_collinear(vertices):
                continue
            # Ensure reasonable area
            area = abs(self._calculate_triangle_area(*vertices))
            if 20 <= area <= 60:
                return vertices

    def _are_collinear(self, points: List[Tuple[int, int]]) -> bool:
        """Check if three points are collinear"""
        (x1, y1), (x2, y2), (x3, y3) = points
        return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < 0.001

    def _calculate_triangle_area(self, p1: Tuple, p2: Tuple, p3: Tuple) -> float:
        """Calculate area of triangle using the shoelace formula"""
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    def _calculate_parallelogram_vertex(self, a: Tuple, b: Tuple, c: Tuple) -> Tuple:
        """Calculate the fourth vertex of a parallelogram using vector addition"""
        # For parallelogram ABCD, we use: D = A + C - B
        return (a[0] + c[0] - b[0], a[1] + c[1] - b[1])

    def _generate_coordinate_distractors(self, correct: Tuple, count: int) -> List[Tuple]:
        """Generate plausible but incorrect coordinate options"""
        x, y = correct
        distractors = []

        # Common mistake patterns
        patterns = [
            (x + random.randint(1, 3), y),  # X-coordinate error
            (x, y + random.randint(1, 3)),  # Y-coordinate error
            (x - random.randint(1, 3), y),  # X-coordinate error (negative)
            (x, y - random.randint(1, 3)),  # Y-coordinate error (negative)
            (-x, y),                        # Sign error in x
            (x, -y),                        # Sign error in y
            (y, x),                         # Coordinate swap
        ]

        # Select unique distractors
        for pattern in patterns:
            if pattern != correct and pattern not in distractors:
                distractors.append(pattern)
                if len(distractors) >= count:
                    break

        return distractors[:count]

    def _generate_detailed_parallelogram_explanation(self, a: Tuple, b: Tuple, c: Tuple,
                                                   d: Tuple, triangle_area: float,
                                                   parallelogram_area: float) -> str:
        """Generate comprehensive explanation with multiple solution methods"""

        explanation = f"""**Solution Method 1: Using Diagonal Intersection Property**

In a parallelogram, the diagonals bisect each other. This means the midpoint of diagonal PR must equal the midpoint of diagonal QS.

Step 1: Find the midpoint of diagonal PR.
Midpoint of PR = $\\left(\\frac{{{a[0]} + {c[0]}}}{2}, \\frac{{{a[1]} + ({c[1]})}}{2}\\right) = \\left(\\frac{{{a[0] + c[0]}}}{2}, \\frac{{{a[1] + c[1]}}}{2}\\right)$

Step 2: Set up equations using the diagonal bisection property.
If S = (x, y), then the midpoint of QS must equal the midpoint of PR.
Midpoint of QS = $\\left(\\frac{{{b[0]} + x}}{2}, \\frac{{{b[1]} + y}}{2}\\right)$

Setting the midpoints equal:
$\\frac{{{b[0]} + x}}{2} = \\frac{{{a[0] + c[0]}}}{2}$ and $\\frac{{{b[1]} + y}}{2} = \\frac{{{a[1] + c[1]}}}{2}$

Solving for x: ${b[0]} + x = {a[0] + c[0]} \\Rightarrow x = {d[0]}$
Solving for y: ${b[1]} + y = {a[1] + c[1]} \\Rightarrow y = {d[1]}$

Therefore, S = {d}

**Solution Method 2: Using Vector Addition Property**

In parallelogram PQRS, we have $\\overrightarrow{{PS}} = \\overrightarrow{{QR}}$ (opposite sides are equal vectors).

$\\overrightarrow{{QR}} = ({c[0]} - {b[0]}, {c[1]} - {b[1]}) = ({c[0] - b[0]}, {c[1] - b[1]})$

If S = (x, y), then $\\overrightarrow{{PS}} = (x - ({a[0]}), y - {a[1]}) = (x + {-a[0]}, y - {a[1]})$

Setting them equal: $(x + {-a[0]}, y - {a[1]}) = ({c[0] - b[0]}, {c[1] - b[1]})$

$x + {-a[0]} = {c[0] - b[0]} \\Rightarrow x = {d[0]}$
$y - {a[1]} = {c[1] - b[1]} \\Rightarrow y = {d[1]}$

This confirms S = {d}

**Area Verification:**

The area of triangle PQR using the shoelace formula:
Area = $\\frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$
     = $\\frac{1}{2}|({a[0]})({b[1]} - ({c[1]})) + ({b[0]})({c[1]} - {a[1]}) + ({c[0]})({a[1]} - {b[1]})|$
     = $\\frac{1}{2}|{triangle_area * 2:.0f}|$
     = {triangle_area:.0f} square units

The area of parallelogram PQRS = 2 × Area of triangle PQR = 2 × {triangle_area:.0f} = {parallelogram_area:.0f} square units

**Alternative Verification using Cross Product:**
We can also verify using the cross product method for parallelogram area:
Area = |$\\overrightarrow{{PQ}} \\times \\overrightarrow{{PS}}$|

$\\overrightarrow{{PQ}} = ({b[0] - a[0]}, {b[1] - a[1]})$
$\\overrightarrow{{PS}} = ({d[0] - a[0]}, {d[1] - a[1]})$

Area = |({b[0] - a[0]}) × ({d[1] - a[1]}) - ({b[1] - a[1]}) × ({d[0] - a[0]})|
     = {parallelogram_area:.0f} square units ✓

This confirms our answer: S = {d} and Area = {parallelogram_area:.0f} square units.
"""
        return explanation

    def generate_complex_word_problem(self, difficulty: DifficultyLevel = DifficultyLevel.HARD) -> QuestionData:
        """
        Generate a sophisticated multi-step word problem involving percentages,
        profit margins, markup calculations, and discount applications
        """
        # Generate realistic business parameters
        items_per_box = random.choice([18, 20, 24, 30])
        base_box_price = round(random.uniform(15.00, 25.00), 2)
        production_cost = round(random.uniform(0.35, 0.55), 2)
        profit_margin = random.choice([30, 35, 40, 45])
        markup_percentage = random.choice([60, 65, 70])
        discount_percentage = random.choice([10, 12, 15])

        # Detailed calculations
        calculations = self._perform_complex_calculations(
            items_per_box, base_box_price, production_cost,
            profit_margin, markup_percentage, discount_percentage
        )

        # Generate question text
        question_text = (
            f"A premium bakery specializes in artisanal cupcakes and operates with a complex "
            f"pricing structure. The bakery sells cupcakes in luxury boxes containing exactly "
            f"{items_per_box} cupcakes each. Each luxury box is priced at ${base_box_price} to "
            f"customers. The bakery's cost analysis shows that each individual cupcake costs "
            f"${production_cost} to produce (including ingredients, labor, and overhead). The "
            f"bakery aims to maintain a gross profit margin of {profit_margin}% on each box sold. "
            f"However, when customers purchase individual cupcakes (not in boxes), the bakery "
            f"applies a premium pricing strategy with a {markup_percentage}% markup over the "
            f"effective per-cupcake cost basis used in box pricing. Additionally, the bakery "
            f"offers a loyalty program where members receive a {discount_percentage}% discount "
            f"on individual cupcakes. Calculate the final price a loyalty program member would "
            f"pay for a single cupcake, and determine how much additional profit the bakery "
            f"makes per cupcake when selling individually to non-members versus selling in boxes."
        )

        # Generate options with realistic variations
        member_price = calculations['member_price']
        additional_profit = calculations['additional_profit']

        options = self._generate_word_problem_options(member_price, additional_profit)
        correct_index = 0  # First option is correct by design

        # Generate comprehensive explanation
        explanation = self._generate_detailed_word_problem_explanation(
            items_per_box, base_box_price, production_cost, profit_margin,
            markup_percentage, discount_percentage, calculations
        )

        return QuestionData(
            question=question_text,
            instruction="Solve this multi-step problem involving percentages, profit margins, markup calculations, and discount applications. Show all intermediate calculations and clearly state your assumptions.",
            options=options,
            correct_answer_index=correct_index,
            explanation=explanation,
            curriculum=CurriculumTopic("Quantitative Math", "Problem Solving", "Problem Solving"),
            difficulty=difficulty,
            latex_expressions=[
                r"\text{Profit Margin} = \frac{\text{Selling Price} - \text{Cost Basis}}{\text{Selling Price}}",
                r"\text{Markup Price} = \text{Cost Basis} \times (1 + \text{Markup Rate})"
            ],
            solution_methods=["Step-by-step algebraic approach", "Working backwards verification", "Profit analysis"],
            common_mistakes=["Confusing profit margin with markup", "Applying discounts to wrong base"],
            prerequisites=["Percentage calculations", "Profit and loss concepts", "Multi-step problem solving"]
        )

    def _perform_complex_calculations(self, items_per_box: int, box_price: float,
                                    production_cost: float, profit_margin: int,
                                    markup_percentage: int, discount_percentage: int) -> Dict[str, float]:
        """Perform all calculations for the word problem with detailed tracking"""

        # Step 1: Calculate total production cost per box
        total_production_cost = items_per_box * production_cost

        # Step 2: Calculate cost basis from profit margin
        # Profit margin = (Selling Price - Cost Basis) / Selling Price
        # Rearranging: Cost Basis = Selling Price × (1 - Profit Margin)
        cost_basis_per_box = box_price * (1 - profit_margin / 100)
        cost_basis_per_cupcake = cost_basis_per_box / items_per_box

        # Step 3: Calculate individual cupcake pricing
        individual_base_price = cost_basis_per_cupcake * (1 + markup_percentage / 100)

        # Step 4: Apply loyalty discount
        member_price = individual_base_price * (1 - discount_percentage / 100)

        # Step 5: Calculate profit comparisons
        profit_per_cupcake_in_box = (box_price / items_per_box) - production_cost
        profit_per_individual_cupcake = individual_base_price - production_cost
        additional_profit = profit_per_individual_cupcake - profit_per_cupcake_in_box

        return {
            'total_production_cost': total_production_cost,
            'cost_basis_per_box': cost_basis_per_box,
            'cost_basis_per_cupcake': cost_basis_per_cupcake,
            'individual_base_price': individual_base_price,
            'member_price': member_price,
            'profit_per_cupcake_in_box': profit_per_cupcake_in_box,
            'profit_per_individual_cupcake': profit_per_individual_cupcake,
            'additional_profit': additional_profit
        }

    def _generate_word_problem_options(self, member_price: float, additional_profit: float) -> List[str]:
        """Generate realistic option choices for the word problem"""

        # Round to nearest cent
        member_price = round(member_price, 2)
        additional_profit = round(additional_profit, 2)

        # Generate variations
        options = [
            f"Member price: ${member_price:.2f}, Additional profit: ${additional_profit:.2f}",
            f"Member price: ${member_price - 0.03:.2f}, Additional profit: ${additional_profit - 0.05:.2f}",
            f"Member price: ${member_price + 0.02:.2f}, Additional profit: ${additional_profit - 0.04:.2f}",
            f"Member price: ${member_price - 0.05:.2f}, Additional profit: ${additional_profit + 0.04:.2f}",
            f"Member price: ${member_price + 0.04:.2f}, Additional profit: ${additional_profit + 0.02:.2f}"
        ]

        return options

    def _generate_detailed_word_problem_explanation(self, items_per_box: int, box_price: float,
                                                  production_cost: float, profit_margin: int,
                                                  markup_percentage: int, discount_percentage: int,
                                                  calculations: Dict[str, float]) -> str:
        """Generate comprehensive step-by-step explanation"""

        explanation = f"""**Step-by-Step Solution:**

**Phase 1: Understanding the Box Economics**

Given information:
- Box contains: {items_per_box} cupcakes
- Box selling price: ${box_price}
- Production cost per cupcake: ${production_cost}
- Target gross profit margin on boxes: {profit_margin}%

Step 1: Calculate total production cost per box
Total production cost = {items_per_box} cupcakes × ${production_cost} = ${calculations['total_production_cost']:.2f}

Step 2: Determine the cost basis for pricing calculations
The profit margin is calculated as: (Selling Price - Cost Basis) ÷ Selling Price

{profit_margin/100:.2f} = (${box_price} - Cost Basis) ÷ ${box_price}
Rearranging: Cost Basis = ${box_price} × (1 - {profit_margin/100:.2f})
Cost Basis = ${box_price} × {1 - profit_margin/100:.2f} = ${calculations['cost_basis_per_box']:.2f}

Step 3: Calculate effective per-cupcake cost basis
Effective per-cupcake cost basis = ${calculations['cost_basis_per_box']:.2f} ÷ {items_per_box} = ${calculations['cost_basis_per_cupcake']:.3f}

**Phase 2: Individual Cupcake Pricing**

Step 4: Apply {markup_percentage}% markup to the effective cost basis
Individual cupcake base price = ${calculations['cost_basis_per_cupcake']:.3f} × (1 + {markup_percentage/100:.2f})
                               = ${calculations['cost_basis_per_cupcake']:.3f} × {1 + markup_percentage/100:.2f}
                               = ${calculations['individual_base_price']:.3f}

Step 5: Calculate loyalty member price ({discount_percentage}% discount)
Member price = ${calculations['individual_base_price']:.3f} × (1 - {discount_percentage/100:.2f})
             = ${calculations['individual_base_price']:.3f} × {1 - discount_percentage/100:.2f}
             = ${calculations['member_price']:.3f}

Rounded to nearest cent: **Member price = ${calculations['member_price']:.2f}**

**Phase 3: Additional Profit Calculation**

Step 6: Calculate profit per cupcake when sold in boxes
Box revenue per cupcake = ${box_price} ÷ {items_per_box} = ${box_price/items_per_box:.3f}
Profit per cupcake in box = ${box_price/items_per_box:.3f} - ${production_cost} = ${calculations['profit_per_cupcake_in_box']:.3f}

Step 7: Calculate profit per individual cupcake (non-member price)
Profit per individual cupcake = ${calculations['individual_base_price']:.3f} - ${production_cost} = ${calculations['profit_per_individual_cupcake']:.3f}

Step 8: Determine additional profit
Additional profit = ${calculations['profit_per_individual_cupcake']:.3f} - ${calculations['profit_per_cupcake_in_box']:.3f} = ${calculations['additional_profit']:.3f}

Rounded to nearest cent: **Additional profit = ${calculations['additional_profit']:.2f}**

**Verification:**
- The {profit_margin}% profit margin on boxes is maintained
- Individual pricing provides premium revenue stream
- Loyalty program balances customer retention with profitability
- Additional profit per individual cupcake justifies the premium pricing strategy

**Final Answer:** Member price: ${calculations['member_price']:.2f}, Additional profit: ${calculations['additional_profit']:.2f}
"""

        return explanation

    def generate_algebraic_expression_question(self, difficulty: DifficultyLevel = DifficultyLevel.MODERATE) -> QuestionData:
        """Generate polynomial expansion and factoring questions"""

        # Generate random coefficients for (ax + b)(cx + d)
        a, b, c, d = [random.randint(-5, 5) for _ in range(4)]
        while a == 0 or c == 0:  # Ensure we have quadratic terms
            a, c = random.randint(-5, 5), random.randint(-5, 5)

        # Create the expression
        expr1 = f"({a}x + {b})" if b >= 0 else f"({a}x - {abs(b)})"
        expr2 = f"({c}x + {d})" if d >= 0 else f"({c}x - {abs(d)})"

        # Calculate expanded form: (ax + b)(cx + d) = acx² + (ad + bc)x + bd
        coeff_x2 = a * c
        coeff_x1 = a * d + b * c
        coeff_x0 = b * d

        # Format the correct answer
        def format_polynomial(c2, c1, c0):
            terms = []
            if c2 != 0:
                if c2 == 1:
                    terms.append("x²")
                elif c2 == -1:
                    terms.append("-x²")
                else:
                    terms.append(f"{c2}x²")

            if c1 != 0:
                if c1 == 1:
                    terms.append("x" if not terms else "+x")
                elif c1 == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{c1:+}x" if terms else f"{c1}x")

            if c0 != 0:
                terms.append(f"{c0:+}" if terms else f"{c0}")

            return "".join(terms) if terms else "0"

        correct_answer = format_polynomial(coeff_x2, coeff_x1, coeff_x0)

        # Generate distractors
        distractors = [
            format_polynomial(coeff_x2, coeff_x1, -coeff_x0),  # Sign error in constant term
            format_polynomial(coeff_x2, -coeff_x1, coeff_x0),  # Sign error in linear term
            format_polynomial(a*c, a+c, b*d),                   # Addition instead of FOIL
            format_polynomial(coeff_x2, coeff_x1 + 2, coeff_x0) # Calculation error
        ]

        options = [correct_answer] + distractors[:4]
        random.shuffle(options)
        correct_index = options.index(correct_answer)

        question_text = f"{expr1}{expr2}\n\nWhich of the following is equivalent to the expression above?"

        explanation = f"""**Using the FOIL Method (First, Outer, Inner, Last):**

Given: {expr1}{expr2}

**First:** {a}x × {c}x = {coeff_x2}x²
**Outer:** {a}x × {d} = {a*d}x
**Inner:** {b} × {c}x = {b*c}x
**Last:** {b} × {d} = {coeff_x0}

Combining like terms:
{coeff_x2}x² + ({a*d}x + {b*c}x) + {coeff_x0}
= {coeff_x2}x² + {coeff_x1}x + {coeff_x0}
= {correct_answer}

**Verification by substitution:**
Let's verify with x = 1:
Original: {expr1}{expr2} = ({a}(1) + {b})({c}(1) + {d}) = ({a + b})({c + d}) = {(a+b)*(c+d)}
Expanded: {correct_answer} = {coeff_x2}(1)² + {coeff_x1}(1) + {coeff_x0} = {coeff_x2 + coeff_x1 + coeff_x0} ✓
"""

        return QuestionData(
            question=question_text,
            instruction="Expand the expression using the distributive property (FOIL method).",
            options=options,
            correct_answer_index=correct_index,
            explanation=explanation,
            curriculum=CurriculumTopic("Quantitative Math", "Algebra", "Polynomial Expressions (FOIL/Factoring)"),
            difficulty=difficulty,
            latex_expressions=[r"(ax + b)(cx + d) = acx^2 + (ad + bc)x + bd"],
            solution_methods=["FOIL Method", "Distributive Property", "Area Model"],
            common_mistakes=["Sign errors", "Forgetting middle terms", "Calculation errors"],
            prerequisites=["Basic algebra", "Distributive property", "Combining like terms"]
        )

    def format_question_output(self, question_data: QuestionData,
                             title: str = "", description: str = "") -> str:
        """Format question according to the specified output format with enhancements"""

        if not question_data.validate():
            raise ValueError("Question data failed validation")

        # Format title and description if provided
        header = ""
        if title:
            header += f"@title {title}\n"
        if description:
            header += f"@description {description}\n\n"

        # Format options with correct answer marking
        options_text = ""
        for i, option in enumerate(question_data.options):
            if i == question_data.correct_answer_index:
                options_text += f"@@option {option}\n"
            else:
                options_text += f"@option {option}\n"

        # Main question format
        question_text = f"""@question {question_data.question}
@instruction {question_data.instruction}
@difficulty {question_data.difficulty.value}
@Order {question_data.order}
{options_text}@explanation
{question_data.explanation}
@subject {question_data.curriculum.subject}
@unit {question_data.curriculum.unit}
@topic {question_data.curriculum.topic}
@plusmarks {question_data.plus_marks}
"""

        return header + question_text

    def generate_comprehensive_assessment(self, num_questions: int = 5,
                                        title: str = "Advanced Math Assessment",
                                        description: str = "Comprehensive assessment covering multiple mathematical domains") -> str:
        """Generate a complete assessment with multiple question types"""

        logger.info(f"Generating comprehensive assessment with {num_questions} questions")

        output = f"@title {title}\n@description {description}\n\n"

        question_generators = [
            self.generate_coordinate_geometry_question,
            self.generate_complex_word_problem,
            self.generate_algebraic_expression_question,
        ]

        for i in range(min(num_questions, len(question_generators))):
            generator = question_generators[i % len(question_generators)]
            question = generator()
            question.order = i + 1
            output += self.format_question_output(question) + "\n"

        logger.info("Assessment generation completed successfully")
        return output

    def export_to_json(self, questions: List[QuestionData], filename: str) -> None:
        """Export questions to JSON format for external processing"""

        def serialize_question(q: QuestionData) -> Dict:
            return {
                'question': q.question,
                'instruction': q.instruction,
                'options': q.options,
                'correct_answer_index': q.correct_answer_index,
                'explanation': q.explanation,
                'curriculum': {
                    'subject': q.curriculum.subject,
                    'unit': q.curriculum.unit,
                    'topic': q.curriculum.topic
                },
                'difficulty': q.difficulty.value,
                'order': q.order,
                'plus_marks': q.plus_marks,
                'latex_expressions': q.latex_expressions,
                'solution_methods': q.solution_methods,
                'common_mistakes': q.common_mistakes,
                'prerequisites': q.prerequisites
            }

        data = {
            'questions': [serialize_question(q) for q in questions],
            'metadata': {
                'total_questions': len(questions),
                'generated_at': str(datetime.datetime.now()),
                'curriculum_coverage': list(set(f"{q.curriculum.subject}→{q.curriculum.unit}→{q.curriculum.topic}" for q in questions))
            }
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        logger.info(f"Questions exported to {filename}")

# Advanced utility functions
def validate_latex_syntax(latex_string: str) -> bool:
    """Validate LaTeX syntax using sympy parsing"""
    try:
        sp.sympify(latex_string.replace(', ', '').replace('\\', '\\\\'))
        return True
    except:
        return False

def generate_question_bank(count: int = 50) -> List[QuestionData]:
    """Generate a large bank of questions for testing purposes"""
    generator = MathQuestionGenerator()
    questions = []

    question_types = [
        generator.generate_coordinate_geometry_question,
        generator.generate_complex_word_problem,
        generator.generate_algebraic_expression_question
    ]

    for i in range(count):
        question_type = question_types[i % len(question_types)]
        difficulty = list(DifficultyLevel)[i % len(DifficultyLevel)]

        question = question_type(difficulty=difficulty)
        question.order = i + 1
        questions.append(question)

    return questions

# Example usage and testing
if __name__ == "__main__":
    import datetime

    print("🧮 Advanced Math Question Generator - Professional Edition")
    print("=" * 60)

    # Initialize generator
    generator = MathQuestionGenerator()

    # Generate comprehensive assessment
    assessment = generator.generate_comprehensive_assessment(
        num_questions=3,
        title="Quantitative Math Mastery Assessment",
        description="Advanced assessment covering coordinate geometry, complex problem solving, and algebraic manipulation"
    )

    print("Generated Assessment:")
    print("-" * 40)
    print(assessment)

    # Save to file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_assessment_{timestamp}.txt"

    with open(filename, "w", encoding='utf-8') as f:
        f.write(assessment)

    print(f"\n✅ Assessment saved to '{filename}'")

    # Generate question bank for testing
    print("\n🏦 Generating question bank...")
    question_bank = generate_question_bank(10)

    # Export to JSON
    json_filename = f"question_bank_{timestamp}.json"
    generator.export_to_json(question_bank, json_filename)

    print(f"✅ Question bank exported to '{json_filename}'")
    print(f"📊 Total questions generated: {len(question_bank)}")

    # Statistics
    difficulty_counts = {}
    topic_counts = {}

    for q in question_bank:
        difficulty_counts[q.difficulty.value] = difficulty_counts.get(q.difficulty.value, 0) + 1
        topic_counts[q.curriculum.topic] = topic_counts.get(q.curriculum.topic, 0) + 1

    print(f"\n📈 Difficulty distribution: {difficulty_counts}")
    print(f"📚 Topic coverage: {topic_counts}")

    print("\n🎯 All operations completed successfully!")
    print("Ready for submission! 🚀")
