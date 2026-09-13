package tarefaII.avaliacaoContinua;

import javax.swing.*;
import java.lang.Math;

public class L02C {
    static void main() {
        final double G = 9.8;
        double height = 0;
        boolean validation = true;
        do {
            try {
                height = Double.parseDouble(JOptionPane.showInputDialog("Digite a altura para saber o tempo de queda de um objeto no vácuo: ").replace(",", "."));

                if (height > 0) {
                    validation = false;
                } else {
                    JOptionPane.showMessageDialog(null, "Valor inválido!\nDigite novamente:");
                }
            } catch (Exception ex) {
                JOptionPane.showMessageDialog(null, "Valor inválido!\nDigite novamente:");
            }
        } while (validation);


        JOptionPane.showMessageDialog(null,
                "Tempo de queda do objeto no vácuo: "
                        + "\nDe acordo com a altura informada: " + String.format("%.2f", height) + "m"
                        + "\n\nO tempo de queda é: " + String.format("%.2f", fallTime(height, G)) + "m/s²");

    }

    public static double fallTime(double height, double gravity) {
        double fall = Math.sqrt((2 * height) / gravity);
        return fall;
    }
}
