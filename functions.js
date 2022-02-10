function gcd(a, b) {
  if(a<b) {
    t = b;
    b = a;
    a = t;
  }
  m = a % b;
  while (m != 0) {
    a = b;
    b = m;
    m = a % b;
  }
  return b;
}

function fmt(i, n) {
  s = "   " + i.toString();
  return s.substr(-3);
}

function ZmZ(m) {
  console.log("ℤ/"+m.toString()+"ℤ");
  s = "|  +  ||";
  t = "––––––||";
  for(i=0; i<m;i++) {
    s += fmt(i, 2) + " |";
    t += "–––––";
  }
  console.log(s);
  console.log(t);
  for(j=0; j<m; j++) {
    s = "| "+ fmt(j, 2)+" ||";
    for(i=0; i<m; i++) {
      x = (i+j) % m;
      s += fmt(x, 3)+" |";
    }
    console.log(s);
  }
  console.log("");

  s = "|  x  ||";
  for(i=0; i<m;i++) {
    s = s + fmt(i, 2) + " |";
  }
  console.log(s);
  console.log(t);
  for(j=0; j<m; j++) {
    s = "| "+ fmt(j, 2)+" ||";
    for(i=0; i<m; i++) {
      x = (i*j) % m;
      s += fmt(x, 3)+" |";
    }
    console.log(s);
  }
  console.log("");

  console.log("(ℤ/"+m.toString()+"ℤ)* =");
  rslt = [];
  for (a = 1; a<m; a++) {
    if (gcd(a, m) == 1) rslt.push(a);
  }
  console.log(rslt);
  s = "|  .  ||";
  t = "––––––||";
  ln = rslt.length;
  for(i=0; i<ln;i++) {
    s += fmt(rslt[i], 2) + " |";
    t += "–––––";
  }
  console.log(s);
  console.log(t);
  for(j=0; j<ln; j++) {
    s = "| "+ fmt(rslt[j], 2)+" ||";
    for(i=0; i<ln; i++) {
      x = (rslt[i]*rslt[j]) % m;
      s += fmt(x, 3)+" |";
    }
    console.log(s);
  }
  console.log("");

}

function fastpow(x, exp, m) {
  if (exp == 1) return x;
  else if (exp % 2) {
    rslt = (x * fastpow(x, exp - 1, m)) % m;
    console.log(exp,"is odd. returning =",rslt);
    return rslt;
  } else {
    rslt = fastpow((x * x) % m, exp / 2, m);
    console.log(exp,"is even. returning =",rslt);
    return rslt;
  }
}

function blocks(x) {
  i = 0;
  rslt = [];
  while (x > 0) {
    if (x % 2) {
      rslt.push(i);
    }
    i += 1;
    x = parseInt(x / 2, 10);
  }
  return rslt;
}

function primeFactors(n) {
  let arr=[];
  let i = 2;
  while(i<=n) {
    if(n%i == 0) {
      n= n/i;
      arr.push(i);
    } else {
      i++;
    }
  }
  const counts = {};
  arr.forEach((x) => {
    counts[x] = (counts[x] || 0) + 1;
  });
  return counts;
}

console.log(primeFactors(1728));
