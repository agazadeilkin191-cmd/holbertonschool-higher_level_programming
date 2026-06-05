#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  // Unikal dəyərlər üçün Set istifadə etmək olar, 
  // lakin tapşırıq sadə sıralama tələb edir
  console.log(sorted[1]);
}
