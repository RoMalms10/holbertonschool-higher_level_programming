#!/usr/bin/node
// Returns the changed version of a list

exports.esrever = function (list) {
  var changed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    changed.push(list[i]);
  }
  return changed;
};
