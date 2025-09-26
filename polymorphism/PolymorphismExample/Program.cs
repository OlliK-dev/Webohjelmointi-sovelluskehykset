
/*



Esimerkissä Area-metodi on polymorfismia käytännössä. 
Sekä kuutio että ympyrä ovat muotoja, 
mutta molemmilla pitää olla oma metodi pinta-alan laskemiselle, 
koska ne lasketaan aivan eri tavoin.



*/

namespace PolymorphismExample2;

public static class Program
{
    public static void Main()
    {
        // huomaa, että ao. rivi on virheellinen
        // koska Shape-luokka on abstrakti, siitä ei voi luoda instanssia
        // instanssin voi luoda vain konkreettisesta luokasta
        // var s = new Shape();

        
        
        var ci = new Circle(5);
        var cia = ci.Area();
        Console.WriteLine(cia);
        
        var cu = new Cube(1,3);
        var cua = cu.Area();
        Console.WriteLine(cua);
    }
}

// luokka on abstrakti, siitä ei voi tehdä instanssia, eikä sillä siksi ole constructoria
public abstract class Shape
{
    // Area-metodilta puuttuu toteutus, koska se on abstrakti
    public abstract double Area();
}


// Cube perii Shape-luokan ja saa constructoriin kaksi parametria
// pinta-alan laskemista varten
public class Cube(double side1, double side2) : Shape
{
    // täällä konkreettisessa luokassa Area-metodi ylikirjoitetaan
    // ja sille tehdään konkreettinen toteutus kuution pinta-alan laskemista varten
    public override double Area()
    {
        return  side1 * side2;
    }
}


// Circle perii Shape-luokan ja saa constructoriin säteen parametrinä
// pinta-alan laskemista varten
public class Circle(double r) : Shape
{
    // täällä konkreettisessa luokassa Area-metodi ylikirjoitetaan
    // ja sille tehdään konkreettinen toteutus ympyrän pinta-alan laskemista varten
    public override double Area()
    {
        return  Math.PI * r * r;
    }
}