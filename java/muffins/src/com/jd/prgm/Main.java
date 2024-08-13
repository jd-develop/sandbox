package com.jd.prgm;

public class Main {
    public static void main(String[] args) {
        double nbreMuffins = calculerMuffins();
        System.out.println("Il y a " + nbreMuffins + " muffins.");
    }

    private static int calculerMuffins() {
        int a = (int)Math.PI;
        double b = Math.PI * 100 - 300;
        int c = (int)b;
        int d = c - 4;
        int e = d / 2;
        return d + e - a;
    }
}

// INDICES
// Math.PI est égal à pi (3.1415926535...)
// (int)nombre renvoie la partie entière du nombre
// System.out.println("mot " + nombre) écrit "mot 3" si nombre est égal à 3
// double désigne un nombre à virgule
