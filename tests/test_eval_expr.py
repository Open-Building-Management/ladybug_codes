"""Unit tests for eval_expr() expression evaluator"""
import pytest
from src.idfhub.common import eval_expr


class TestEvalExprBasicArithmetic:
    """Test basic arithmetic operations"""

    def test_addition(self):
        """Test addition of numbers"""
        assert eval_expr("2+3", {}) == 5
        assert eval_expr("altitude+2", {"altitude": 0}) == 2
        assert eval_expr("altitude+2", {"altitude": 3}) == 5

    def test_subtraction(self):
        """Test subtraction of numbers"""
        assert eval_expr("5-2", {}) == 3
        assert eval_expr("altitude-1", {"altitude": 5}) == 4
        assert eval_expr("0-5", {}) == -5

    def test_multiplication(self):
        """Test multiplication of numbers"""
        assert eval_expr("3*4", {}) == 12
        assert eval_expr("altitude*2", {"altitude": 3}) == 6
        assert eval_expr("height*2", {"height": 1.5}) == 3.0

    def test_division(self):
        """Test division of numbers"""
        assert eval_expr("10/2", {}) == 5
        assert eval_expr("altitude/2", {"altitude": 10}) == 5.0
        assert eval_expr("height/4", {"height": 1.6}) == 0.4

    def test_unary_negation(self):
        """Test unary minus operator"""
        assert eval_expr("-5", {}) == -5
        assert eval_expr("-altitude", {"altitude": 5}) == -5

    def test_unary_plus(self):
        """Test unary plus operator"""
        assert eval_expr("+5", {}) == 5
        assert eval_expr("+altitude", {"altitude": 5}) == 5


class TestEvalExprMultipleVariables:
    """Test expressions with multiple variables"""

    def test_two_variables_addition(self):
        """Test addition with two variables"""
        assert eval_expr("altitude+height", {"altitude": 0, "height": 3}) == 3

    def test_two_variables_subtraction(self):
        """Test subtraction with two variables"""
        assert eval_expr("height-altitude", {"altitude": 0, "height": 3}) == 3

    def test_multiple_operations(self):
        """Test chained operations"""
        assert eval_expr("altitude+height+1", {"altitude": 0, "height": 3}) == 4
        assert eval_expr("2*altitude+height", {"altitude": 2, "height": 3}) == 7

    def test_operator_precedence(self):
        """Test multiplication/division precedence over addition/subtraction"""
        assert eval_expr("2+3*4", {}) == 14
        assert eval_expr("altitude*2+height", {"altitude": 2, "height": 3}) == 7
        assert eval_expr("altitude+height*2", {"altitude": 1, "height": 2}) == 5


class TestEvalExprEdgeCases:
    """Test edge cases and boundary conditions"""

    def test_zero(self):
        """Test with zero values"""
        assert eval_expr("0", {}) == 0
        assert eval_expr("altitude+0", {"altitude": 5}) == 5

    def test_negative_numbers(self):
        """Test with negative numbers"""
        assert eval_expr("-5+3", {}) == -2
        assert eval_expr("altitude+-2", {"altitude": 3}) == 1

    def test_floats(self):
        """Test floating point arithmetic"""
        assert eval_expr("1.5+2.5", {}) == 4.0
        assert eval_expr("altitude/2", {"altitude": 5}) == 2.5

    def test_large_numbers(self):
        """Test with large numbers"""
        assert eval_expr("1000000+1000000", {}) == 2000000
        assert eval_expr("altitude*1000", {"altitude": 999}) == 999000

    def test_whitespace_handling(self):
        """Test expressions with various whitespace"""
        assert eval_expr("2 + 3", {}) == 5
        assert eval_expr("altitude + 2", {"altitude": 3}) == 5
        assert eval_expr("  altitude  +  2  ", {"altitude": 3}) == 5


class TestEvalExprErrors:
    """Test error handling and invalid inputs"""

    def test_undefined_variable(self):
        """Test that undefined variable raises KeyError"""
        with pytest.raises(KeyError):
            eval_expr("undefined_var", {})

    def test_unsupported_operation(self):
        """Test that unsupported operations raise TypeError"""
        # Boolean 'or' is not supported
        with pytest.raises(TypeError):
            eval_expr("altitude or True", {"altitude": 5})

        # Boolean 'and' is not supported
        with pytest.raises(TypeError):
            eval_expr("altitude and True", {"altitude": 5})

    def test_function_call_injection(self):
        """Test that function calls are blocked"""
        # Attempting to call a function should fail
        with pytest.raises((TypeError, AttributeError)):
            eval_expr("len([1,2,3])", {})

    def test_import_injection(self):
        """Test that import statements are blocked"""
        # This should be caught by ast parsing (can't import in expression mode)
        with pytest.raises(TypeError):
            eval_expr("__import__('os')", {})

    def test_attribute_access_injection(self):
        """Test that attribute access is blocked"""
        # Attribute access is not supported in the evaluator
        with pytest.raises(TypeError):
            eval_expr("altitude.imag", {"altitude": 5})

    def test_comparison_not_supported(self):
        """Test that comparison operators are not supported"""
        with pytest.raises(TypeError):
            eval_expr("altitude > 5", {"altitude": 10})

    def test_empty_expression(self):
        """Test that empty expression raises error"""
        with pytest.raises((ValueError, SyntaxError)):
            eval_expr("", {})


class TestEvalExprRealWorldScenarios:
    """Test real-world geometry scenarios from the YAML config"""

    def test_altitude_plus_height(self):
        """Test geometry formula: altitude+2 (door top from sill)"""
        # From agence.yml: [10, 11, "altitude+2"]
        result = eval_expr("altitude+2", {"altitude": -3})
        assert result == -1

    def test_altitude_with_different_levels(self):
        """Test altitude expressions for different building levels"""
        # Ground floor
        assert eval_expr("altitude", {"altitude": 0}) == 0
        # Basement
        assert eval_expr("altitude", {"altitude": -3}) == -3
        # First floor
        assert eval_expr("altitude", {"altitude": 3}) == 3

    def test_height_scaling(self):
        """Test scaling heights (e.g., window width scaling)"""
        assert eval_expr("width*2", {"width": 1.2}) == 2.4
        assert eval_expr("height*0.5", {"height": 2}) == 1.0

    def test_combined_geometry_formula(self):
        """Test combined altitude and height formula"""
        variables = {"altitude": 0, "height": 3}
        # Top of a wall element
        assert eval_expr("altitude+height", variables) == 3
        # Bottom of a door with sill
        assert eval_expr("altitude+height-2", variables) == 1
