from sure import expect

from ..recursion import get_fib


def test_get_fib():
    expect(get_fib(0)).to.equal(0)
    expect(get_fib(1)).to.equal(1)
    expect(get_fib(5)).to.equal(5)
    expect(get_fib(10)).to.equal(55)
    expect(get_fib(15)).to.equal(610)
    expect(get_fib(20)).to.equal(6765)

    expect(get_fib).when.called_with(-1).to.throw(ValueError)
    expect(get_fib).when.called_with(-10).to.throw(ValueError)
