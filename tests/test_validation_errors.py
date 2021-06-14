from baby_steps import given, then, when
from district42.types import IntSchema
from th import PathHolder

from valera.errors import (
    AlphabetValidationError,
    ExtraElementValidationError,
    ExtraKeyValidationError,
    IndexValidationError,
    LengthValidationError,
    MaxLengthValidationError,
    MaxValueValidationError,
    MinLengthValidationError,
    MinValueValidationError,
    SchemaMismatchValidationError,
    TypeValidationError,
    ValueValidationError,
)


def test_validation_type_error():
    with when:
        res = TypeValidationError(PathHolder(), "banana", int)

    with then:
        assert repr(res) == "TypeValidationError(PathHolder(), 'banana', <class 'int'>)"


def test_validation_value_error():
    with given:
        actual = "banana"
        expected = "cucumber"

    with when:
        res = ValueValidationError(PathHolder(), actual, expected)

    with then:
        assert repr(res) == "ValueValidationError(PathHolder(), 'banana', 'cucumber')"


def test_validation_min_value_error():
    with when:
        res = MinValueValidationError(PathHolder(), 41, 42)

    with then:
        assert repr(res) == "MinValueValidationError(PathHolder(), 41, 42)"


def test_validation_max_value_error():
    with when:
        res = MaxValueValidationError(PathHolder(), 43, 42)

    with then:
        assert repr(res) == "MaxValueValidationError(PathHolder(), 43, 42)"


def test_validation_len_error():
    with when:
        res = LengthValidationError(PathHolder(), "banana", 7)

    with then:
        assert repr(res) == "LengthValidationError(PathHolder(), 'banana', 7)"


def test_validation_min_len_error():
    with when:
        res = MinLengthValidationError(PathHolder(), "banana", 7)

    with then:
        assert repr(res) == "MinLengthValidationError(PathHolder(), 'banana', 7)"


def test_validation_max_len_error():
    with when:
        res = MaxLengthValidationError(PathHolder(), "banana", 7)

    with then:
        assert repr(res) == "MaxLengthValidationError(PathHolder(), 'banana', 7)"


def test_validation_alphabet_error():
    with when:
        res = AlphabetValidationError(PathHolder(), "banana!", "abn")

    with then:
        assert repr(res) == "AlphabetValidationError(PathHolder(), 'banana!', 'abn')"


def test_validation_index_error():
    with when:
        res = IndexValidationError(PathHolder(), 0)

    with then:
        assert repr(res) == "IndexValidationError(PathHolder(), 0)"


def test_validation_extra_element_error():
    with when:
        res = ExtraElementValidationError(PathHolder(), 0)

    with then:
        assert repr(res) == "ExtraElementValidationError(PathHolder(), 0)"


def test_validation_extra_key_error():
    with when:
        res = ExtraKeyValidationError(PathHolder(), "key")

    with then:
        assert repr(res) == "ExtraKeyValidationError(PathHolder(), 'key')"


def test_validation_schema_mismatch_error():
    with when:
        res = SchemaMismatchValidationError(PathHolder(), "key", (IntSchema(),))

    with then:
        assert repr(res) == "SchemaMismatchValidationError(PathHolder(), 'key', (schema.int,))"