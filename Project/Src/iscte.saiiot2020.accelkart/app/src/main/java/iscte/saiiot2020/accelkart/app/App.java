/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package iscte.saiiot2020.accelkart.app;

import iscte.saiiot2020.accelkart.list.LinkedList;

import static iscte.saiiot2020.accelkart.utilities.StringUtils.join;
import static iscte.saiiot2020.accelkart.utilities.StringUtils.split;
import static iscte.saiiot2020.accelkart.app.MessageUtils.getMessage;

public class App {
    public static void main(String[] args) {
        LinkedList tokens;
        tokens = split(getMessage());
        System.out.println(join(tokens));
    }
}
