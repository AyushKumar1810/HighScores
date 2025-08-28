#!/usr/bin/env python3
"""
Math Question Generator
Generates similar math questions based on base question patterns
Author: AI Assistant
Date: August 2025
"""

import random
import math
from typing import List, Dict, Tuple
import json

class MathQuestionGenerator:
    """
    A class to generate math questions following specific curriculum patterns
    """
    
    def __init__(self):
        self.curriculum = {
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
        
    def generate_coordinate_geometry_question(self) -> Dict:
        """
        Generate a coordinate geometry question about parallelograms
        """
        # Generate random coordinates for three vertices
        vertices = [
            (random.randint(-8, 8), random.randint(-8, 8)),
            (random.randint(-8, 8), random.randint(-8, 8)),
            (random.randint(-8, 8), random.randint(-8, 8))
        ]
        
        # Calculate the fourth vertex for parallelogram
        # Using property: A + C = B + D for parallelogram ABCD
        a, b, c = vertices
        d = (a[0] + c[0] - b[0], a[1] + c[1] - b[1])
        
        # Generate distractors
        distractors = [
            (d[0] + random.randint(1, 3), d[1]),
            (d[0], d[1] + random.randint(1, 3)),
            (d[0] - random.randint(1, 3), d[1]),
            (d[0], d[1] - random.randint(1, 3))
        ]
        
        options = [d] + distractors[:4]
        random.shuffle(options)
        correct_index = options.index(d)
        
        question_data = {
            "question": f"In the coordinate plane, triangle ABC has vertices at A{a}, B{b}, and C{c}. If point D is located such that ABCD forms a parallelogram, what are the coordinates of point D?",
            "options": [f"{opt}" for opt in options],
            "correct_answer": correct_index,
            "explanation": self._generate_parallelogram_explanation(a, b, c, d),
            "subject": "Quantitative Math",
            "unit": "Geometry and Measurement",
            "topic": "Coordinate Geometry",
            "difficulty": "moderate"
        }
        
        return question_data
    
    def _generate_parallelogram_explanation(self, a: Tuple, b: Tuple, c: Tuple, d: Tuple) -> str:
        """Generate explanation for parallelogram question"""
        return f"""
        In a parallelogram, opposite sides are parallel and equal in length. We can use the property 
        that the diagonals of a parallelogram bisect each other.
        
        For parallelogram ABCD, the midpoint of diagonal AC must equal the midpoint of diagonal BD.
        
        Midpoint of AC = (({a[0]} + {c[0]})/2, ({a[1]} + {c[1]})/2) = ({(a[0] + c[0])/2}, {(a[1] + c[1])/2})
        
        If D = (x, y), then midpoint of BD = (({b[0]} + x)/2, ({b[1]} + y)/2)
        
        Setting them equal:
        ({b[0]} + x)/2 = {(a[0] + c[0])/2} → x = {d[0]}
        ({b[1]} + y)/2 = {(a[1] + c[1])/2} → y = {d[1]}
        
        Therefore, D = {d}
        """
    
    def generate_word_problem_question(self) -> Dict:
        """
        Generate a complex word problem involving percentages and markup
        """
        # Random parameters for the problem
        items_per_box = random.choice([12, 15, 18, 20, 24])
        box_price = round(random.uniform(8.00, 15.00), 2)
        cost_per_item = round(random.uniform(0.25, 0.50), 2)
        profit_percentage = random.choice([30, 35, 40, 45])
        markup_percentage = random.choice([40, 45, 50, 55])
        
        # Calculate correct answer
        cost_basis_per_item = (cost_per_item * items_per_box) / items_per_box * (100 / (100 + profit_percentage))
        individual_price = cost_basis_per_item * (1 + markup_percentage/100)
        individual_price = round(individual_price, 2)
        
        # Generate distractors
        distractors = [
            round(cost_per_item * 1.5, 2),
            round((box_price / items_per_box) * 1.2, 2),
            round(cost_per_item * (1 + markup_percentage/100), 2),
            round((box_price / items_per_box) * (1 + markup_percentage/100), 2)
        ]
        
        # Remove duplicates and ensure we have enough options
        all_options = list(set([individual_price] + distractors))
        while len(all_options) < 5:
            all_options.append(round(individual_price + random.uniform(-0.2, 0.2), 2))
        
        options = all_options[:5]
        random.shuffle(options)
        correct_index = options.index(individual_price)
        
        question_data = {
            "question": f"A bakery sells cupcakes in boxes. Each box contains {items_per_box} cupcakes and costs ${box_price}. If the bakery needs to make a profit of {profit_percentage}% on each box and the cost to make each cupcake is ${cost_per_item}, what should be the selling price per individual cupcake when sold separately? (Assume individual cupcakes have a {markup_percentage}% markup over the per-cupcake cost in a box)",
            "options": [f"${opt:.2f}" for opt in options],
            "correct_answer": correct_index,
            "explanation": self._generate_word_problem_explanation(
                items_per_box, box_price, cost_per_item, profit_percentage, 
                markup_percentage, individual_price
            ),
            "subject": "Quantitative Math",
            "unit": "Problem Solving", 
            "topic": "Problem Solving",
            "difficulty": "hard"
        }
        
        return question_data
    
    def _generate_word_problem_explanation(self, items_per_box: int, box_price: float, 
                                         cost_per_item: float, profit_percentage: int,
                                         markup_percentage: int, answer: float) -> str:
        """Generate explanation for word problem"""
        total_cost = items_per_box * cost_per_item
        cost_basis = total_cost / (1 + profit_percentage/100)
        cost_basis_per_item = cost_basis / items_per_box
        
        return f"""
        Step 1: Find the cost basis for the box.
        Total cost to make {items_per_box} cupcakes = {items_per_box} × ${cost_per_item} = ${total_cost}
        
        Step 2: The bakery makes {profit_percentage}% profit on boxes selling at ${box_price}.
        If cost basis × (1 + {profit_percentage}%) = ${box_price}
        Then cost basis = ${box_price} ÷ 1.{profit_percentage} = ${cost_basis:.2f}
        
        Step 3: Cost basis per cupcake = ${cost_basis:.2f} ÷ {items_per_box} = ${cost_basis_per_item:.2f}
        
        Step 4: Individual cupcakes have {markup_percentage}% markup over cost basis.
        Individual price = ${cost_basis_per_item:.2f} × (1 + {markup_percentage}%) = ${answer:.2f}
        """
    
    def format_question_output(self, question_data: Dict, order: int) -> str:
        """
        Format question according to the specified output format
        """
        options_text = ""
        for i, option in enumerate(question_data["options"]):
            if i == question_data["correct_answer"]:
                options_text += f"@@option {option}\n"
            else:
                options_text += f"@option {option}\n"
        
        return f"""
@question {question_data["question"]}
@instruction Choose the correct answer.
@difficulty {question_data["difficulty"]}
@Order {order}
{options_text}@explanation 
{question_data["explanation"]}
@subject {question_data["subject"]}
@unit {question_data["unit"]}
@topic {question_data["topic"]}
@plusmarks 1
"""

    def generate_assessment(self, title: str = "Generated Math Assessment", 
                           description: str = "Auto-generated math assessment") -> str:
        """
        Generate a complete assessment with multiple questions
        """
        output = f"@title {title}\n@description {description}\n\n"
        
        # Generate coordinate geometry question
        coord_question = self.generate_coordinate_geometry_question()
        output += self.format_question_output(coord_question, 1)
        
        # Generate word problem question  
        word_question = self.generate_word_problem_question()
        output += self.format_question_output(word_question, 2)
        
        return output

# Example usage
if __name__ == "__main__":
    generator = MathQuestionGenerator()
    assessment = generator.generate_assessment()
    print(assessment)
    
    # Save to file
    with open("generated_assessment.txt", "w") as f:
        f.write(assessment)
    
    print("Assessment generated and saved to 'generated_assessment.txt'")
