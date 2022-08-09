var keys = ['foo', 'bar', 'baz'];
var values = [11, 22, 33]

var result = {};
keys.forEach((key, i) => result[key] = values[i]);
console.log(result);