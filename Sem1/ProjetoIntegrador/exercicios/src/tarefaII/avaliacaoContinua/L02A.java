//a) area do triangulo: area = base X altura / 2
package tarefaII.avaliacaoContinua;

import javax.swing.*;

public class L02A {
    static void main() {
        double area, base = 0, altura = 0;
        boolean validation = true;

        do {
            try {

                base = Double.parseDouble(JOptionPane.showInputDialog("Informe o Base: ").replace(",", "."));
                if (base > 0) {
                    while (validation) {
                        try {
                            altura = Double.parseDouble(JOptionPane.showInputDialog("Informe a Altura: ").replace(",", "."));
                            if (altura > 0) {
                                validation = false;
                            } else {
                                JOptionPane.showMessageDialog(null, "Valor da Altura inválido, digite novamente");
                            }
                        } catch (NumberFormatException e) {
                            JOptionPane.showMessageDialog(null, "Valor da Altura inválido, digite novamente");
                        }
                    }
                }
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Valor da base inválido, digite novamente");
            }
        } while (validation);

        area = triangleArea(base, altura);

        JOptionPane.showMessageDialog(null, "De acordo com os valores informados:\n "
                + "\nO valor da base: " + String.format("%.2f", base) + "m;"
                + "\nO valor da altura: " + String.format("%.2f", altura) + "m;"
                + "\n\nA área do triangulo é: " + String.format("%.2f", area) + "m²;");


    }

    public static double triangleArea(double base, double height) {
        double area = (base * (height / 2));
        return area;
    }
}
