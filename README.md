# Math Question Generator 🧮

An intelligent system for generating high-quality mathematics assessment questions following standardized curriculum patterns.

## 🎯 Project Overview

This project creates similar mathematics questions based on existing question patterns, maintaining educational rigor while providing variety in assessment content. The system follows strict curriculum alignment and generates questions in the standardized format required for educational assessments.

## ✨ Features

- **Curriculum-Aligned**: All questions strictly follow the provided curriculum hierarchy (Subject → Unit → Topic)
- **Multiple Question Types**: Supports coordinate geometry, word problems, algebraic expressions, and more
- **Standardized Format**: Generates questions in the exact format specification provided
- **Automatic Explanations**: Creates detailed step-by-step explanations for each question
- **Difficulty Scaling**: Supports easy, moderate, and hard difficulty levels
- **LaTeX Support**: Preserves mathematical expressions in LaTeX format
- **Image Generation Ready**: Structured to support coordinate plane and geometric figure generation

## 📚 Supported Curriculum Areas

### Quantitative Math
- **Problem Solving**: Numbers and Operations, Algebra, Geometry, Probability and Statistics, Data Analysis
- **Algebra**: Algebraic Word Problems, Polynomial Expressions, Quadratic Equations, Functions
- **Geometry and Measurement**: Coordinate Geometry, Area & Volume, Trigonometry, Transformations
- **Numbers and Operations**: Fractions, Decimals, Percentages, Number Theory
- **Data Analysis & Probability**: Statistical Analysis, Probability, Graphical Interpretation
- **Reasoning**: Complex Word Problems

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Required packages: `random`, `math`, `typing`, `json`

### Installation
```bash
git clone https://github.com/yourusername/math-question-generator.git
cd math-question-generator
pip install -r requirements.txt
```

### Basic Usage
```python
from math_generator import MathQuestionGenerator

generator = MathQuestionGenerator()
assessment = generator.generate_assessment(
    title="Quantitative Math Practice Test",
    description="Comprehensive assessment covering coordinate geometry and problem solving"
)
print(assessment)
```

## 📖 Question Format

Each generated question follows this exact format:

```
@title Assessment title
@description Assessment description

@question Write your question here
@instruction Write instruction here  
@difficulty easy,moderate,hard
@Order Question number
@option write first option here
@option Write second option here
@@option Correct Answer
@option option
@explanation 
Write your question explanation here
@subject Write subject of the question here
@unit Write unit of the subject
@topic Write topic of the question
@plusmarks 1
```

## 🧠 Question Types Generated

### 1. Coordinate Geometry Questions
- Parallelogram completion problems
- Distance and midpoint calculations
- Slope and line equations
- Geometric transformations

**Example:**
```
In the coordinate plane, triangle ABC has vertices at A(-2, 4), B(6, 1), and C(2, -3). 
If point D is located such that ABCD forms a parallelogram, what are the coordinates of point D?
```

### 2. Complex Word Problems  
- Multi-step percentage problems
- Profit and markup calculations
- Rate and proportion problems
- Real-world applications

**Example:**
```
A bakery sells cupcakes in boxes. Each box contains 18 cupcakes and costs $12.60. 
If the bakery needs to make a profit of 40% on each box and the cost to make each 
cupcake is $0.35, what should be the selling price per individual cupcake when sold 
separately?
```

## 🔧 Advanced Features

### Custom Question Generation
```python
# Generate specific question types
coord_question = generator.generate_coordinate_geometry_question()
word_question = generator.generate_word_problem_question()

# Format according to standards
formatted = generator.format_question_output(coord_question, 1)
```

### Curriculum Validation
The system ensures all questions align with the provided curriculum structure:
- Validates subject-unit-topic hierarchy
- Maintains educational standards
- Ensures appropriate difficulty progression

### Explanation Generation
Each question includes comprehensive explanations:
- Step-by-step solution process
- Mathematical reasoning
- Alternative solution methods
- Common mistake identification

## 📊 Quality Assurance

- **Mathematical Accuracy**: All calculations verified through multiple methods
- **Curriculum Alignment**: Strict adherence to provided curriculum standards  
- **Format Compliance**: Perfect matching of required output format
- **Difficulty Calibration**: Appropriate challenge level for target audience
- **Explanation Quality**: Clear, educational explanations with proper mathematical notation

## 🎨 Image Generation Support

The system is designed to work with mathematical figure generation:
- Coordinate plane visualizations
- Geometric shape illustrations  
- Graph and chart representations
- Diagram annotations and labels

## 📝 Sample Output

```
@title Quantitative Math Problem Solving Assessment
@description This assessment evaluates students' problem-solving abilities across various mathematical domains.

@question In the coordinate plane, triangle ABC has vertices at A(-2, 4), B(6, 1), and C(2, -3). If point D is located such that ABCD forms a parallelogram, what are the coordinates of point D?
@instruction Choose the correct coordinates for point D that would complete the parallelogram ABCD.
@difficulty moderate
@Order 1
@option (-6, 0)
@option (-2, -6)
@@option (-6, 2)  
@option (2, 6)
@option (0, -2)
@explanation 
In a parallelogram, opposite sides are parallel and equal in length. Using the diagonal midpoint property...
[Detailed mathematical explanation continues]
@subject Quantitative Math
@unit Geometry and Measurement
@topic Coordinate Geometry
@plusmarks 1
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Educational assessment standards and best practices
- Curriculum alignment requirements
- Mathematical accuracy verification methods
- LaTeX mathematical notation standards

## 📞 Contact

For questions or support, please open an issue in the repository or contact the development team.

---
**Built with ❤️ for mathematics education**
