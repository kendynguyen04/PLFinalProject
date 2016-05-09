/**
 * Created by Ken on 5/6/2016.
 */
public class Character {
    private String name;
    private int age;
    private String memDate;
    private String race;
    private String role;
    private int level;

    public Character(String s, int a, String d, String r1, String r2, int l) {
        this.name = s;
        this.age = a;
        this.memDate = d;
        this.race = r1;
        this.role = r2;
        this.level = l;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getDate() {
        return memDate;
    }

    public String getRace() {
        return race;
    }

    public String getRole() {
        return role;
    }

    public int getLevel() {
        return level;
    }
}
