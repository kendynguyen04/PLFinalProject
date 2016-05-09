import java.util.ArrayList;
import java.util.stream.Collectors;

/**
 * Created by Ken on 5/6/2016.
 */
public class Guild {

    public static void processGuild() {

        // character format: name, age, membership_date, race, role, level
        ArrayList<Character> roster = new ArrayList<>();
        Character e1 = new Character("MICHAEL", 22, "3-MAR-90", "ELF", "FIGHTER", 89);
        Character e2 = new Character("JACKIE", 17, "27-FEB-91", "HUMAN", "FIGHTER", 78);
        Character e3 = new Character("CHRIS", 20, "14-MAY-90", "HUMAN", "TANK", 92);
        Character e4 = new Character("GILSON", 16, "18-JAN-92", "DWARF", "FIGHTER", 88);
        Character e5 = new Character("SANDERS", 19, "18-FEB-91", "HUMAN", "TANK", 91);
        Character e6 = new Character("DAMERON", 18, "9-OCT-91", "ELF", "FIGHTER", 67);
        Character e7 = new Character("HARDWICK", 19, "7-FEB-92", "ELF", "HEALER", 74);
        Character e8 = new Character("BROWN", 21, "8-MAR-90", "DWARF", "FIGHTER", 76);
        Character e9 = new Character("WILLIAM", 16, "9-FEB-91", "HUMAN", "TANK", 82);
        Character e10 = new Character("PATRICK", 17, "6-AUG-91", "ELF", "HEALER", 75);
        Character e11 = new Character("BELL", 23, "26-MAY-91", "DWARF", "HEALER", 80);
        Character e12 = new Character("SMITH", 24, "8-MAR-90", "HUMAN", "FIGHTER", 63);
        Character e13 = new Character("GANTOS", 25, "30-NOV-90", "ELF", "HEALER", 99);
        Character e14 = new Character("STEPHEN", 22, "17-MAR-91", "ELF", "TANK", 74);
        Character e15 = new Character("CHESTER", 18, "30-NOV-90", "HUMAN", "FIGHTER", 86);
        Character e16 = new Character("PEARL", 19, "17-OCT-90", "DWARF", "TANK", 83);
        Character e17 = new Character("DANCER", 16, "17-MAR-91", "HUMAN", "HEALER", 77);
        Character e18 = new Character("SCHMITT", 14, "9-MAY-91", "ELF", "HEALER", 99);
        Character e19 = new Character("NORTON", 19, "17-JUN-91", "HUMAN", "FIGHTER", 81);
        Character e20 = new Character("QUENTIN", 18, "7-APR-90", "ELF", "FIGHTER", 85);

        roster.add(e1);
        roster.add(e2);
        roster.add(e3);
        roster.add(e4);
        roster.add(e5);
        roster.add(e6);
        roster.add(e7);
        roster.add(e8);
        roster.add(e9);
        roster.add(e10);
        roster.add(e11);
        roster.add(e12);
        roster.add(e13);
        roster.add(e14);
        roster.add(e15);
        roster.add(e16);
        roster.add(e17);
        roster.add(e18);
        roster.add(e19);
        roster.add(e20);

        System.out.println("\nSELECT name, race, level FROM roster GROUP BY race ORDER BY level");
        roster.stream()
                .collect(Collectors.groupingBy(Character::getRace))
                .entrySet()
                .stream()
                .map(k -> k.getValue())
                .forEach((l) -> {
                    l.stream().sorted((p1, p2) -> Integer.compare(p1.getLevel(),p2.getLevel()))
                            .forEach(e -> {
                                String toPrint = e.getName() + " " + e.getRace() + " " + e.getLevel();
                                System.out.println(toPrint);
                            });
                });

        System.out.println("\nSELECT name, role, level FROM roster GROUP BY role WHERE level > 80");
        roster.stream()
                .collect(Collectors.groupingBy(Character::getRole))
                .entrySet()
                .stream()
                .map(k -> k.getValue())
                .forEach((l) -> {
                    l.stream().filter(e -> (e.getLevel() > 80))
                            .forEach(e -> {
                                String toPrint = e.getName() + " " + e.getRole() + " " + e.getLevel();
                                System.out.println(toPrint);
                            });
                });

        System.out.println("\nSELECT name, age, membership_date FROM roster ORDER BY age");
        roster.stream()
                .sorted((p1, p2) -> Integer.compare(p1.getAge(), p2.getAge()))
                .forEach(e -> {
                    String toPrint = e.getName() + " " + e.getAge() + " " + e.getDate();
                    System.out.println(toPrint);
                });


        System.out.println("\nSELECT name, age, race, level FROM roster ORDER BY name");
        roster.stream()
                .sorted((p1, p2) -> p1.getName().compareTo(p2.getName()))
                .forEach(e -> {
                    String toPrint = e.getName() + " " + e.getAge() + " " + e.getRace() + " " + e.getLevel();
                    System.out.println(toPrint);
                });
    }
}
