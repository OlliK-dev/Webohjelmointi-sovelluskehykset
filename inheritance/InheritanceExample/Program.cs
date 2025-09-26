// Voit luoda uuden konsolisovelluksen dotnet cli:llä näin

// dotnet new console -n InheritanceExample1

namespace InheritanceExample1;

public static class Program
{
    public static void Main(string[] args)
    {
        var r = new Runner("Jessi", "Juoksija");
        r.Run();

        var c = new Cyclist("Pera", "Pyöräilijä");
            
        c.Cycle();
    }
}
    
// c#:ssa yliluokka pitää merkitä publicksi, jotta sen voi periä
// Athelete(string firstname, string lastname) on luokan constructor
public class Athlete(string firstname, string lastname)
{
    // Firstname property on merkitty privaatiksi,
    // koska siihen ei tarvitse päästä käsiksi tämän luokan ulkopuolelta
    
    // asetetaan Firstnamen arvoksi costructorin parametri firstname
    private string Firstname { get; } = firstname;
    
    // Lastname property on merkitty privaatiksi,
    // koska siihen ei tarvitse päästä käsiksi tämän luokan ulkopuolelta
    
    // asetetaan Lastnamen arvoksi costructorin parametri lastname
    private string Lastname { get; } = lastname;
    
    
    // Tehdään Greeting()sta protected-tason metodi, koska sitä käytetään perivissä luokissa Runner ja Cyclist
    protected void Greeting()
    {
        Console.WriteLine("Hello my name is {0} {1}", Firstname, Lastname);
    }
}

// Runner-luokka perii Athelete-luokan samalla
// tässä: Athlete(firstname, lastname) kutsutaan Athelete-luokan constructoria samoilla parametreilla, jotka 
// Runner-luokalle annetaan
public class Runner(string firstname, string lastname) : Athlete(firstname, lastname)
{
    public void Run()
    {
        // Greeting-metodia voi käyttää täällä, koska se tulee perittynä Athlete-luokalta
        Greeting();
        Console.WriteLine("I'm running");
    }
}

// Cyclist-luokka perii Athelete-luokan samalla
// tässä: Athlete(firstname, lastname) kutsutaan Athelete-luokan constructoria samoilla parametreilla, jotka 
// Cyclist-luokalle annetaan
public class Cyclist(string firstname, string lastname) : Athlete(firstname, lastname) {

    public void Cycle()
    {
        // Greeting-metodia voi käyttää täällä, koska se tulee perittynä Athlete-luokalta
        Greeting();
        Console.WriteLine("I'm cycling");
    }
}