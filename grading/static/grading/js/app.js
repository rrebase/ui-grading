// noinspection JSUnresolvedFunction
const myapp = new Vue({
  el: '#app',
  data: {
    total: 12,
    inputs: ["a", "b"]
  },
  methods: {
    incrementTotal: function (event) {
      this.total += 1;
    },
    decrementTotal: function () {
      this.total -= 1;
    }
  },
});


Vue.options.delimiters = ['[', ']'];
