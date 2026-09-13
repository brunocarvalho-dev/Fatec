//b)Distância de um raio: distancia = tempo X 360metros/segundo
package tarefaII.avaliacaoContinua;

import javax.swing.*;

public class L02B {
    public static void main(String[] args) {
        boolean validation = true;
        int secunds = 0;
        double distancia;
        do {
            try {
                secunds = Integer.parseInt(JOptionPane.showInputDialog("Digite o valor em segundos, para saber a distância do raio").replace(",",""));
                if (secunds > 0) {
                    validation = false;
                }else {
                    JOptionPane.showMessageDialog(null, "Valor digitado invalido, tente novamente: ");
                }
                } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Valor digitado invalido, tente novamente: ");
            }
        }while (validation);

        distancia = lightningStrikeDistance(secunds);
        JOptionPane.showMessageDialog(null,
                "\nO som viaja a 360m/s;"
                        +"\nComo o som do raio foi ouvido "+secunds+" segundos após ser visto,"
                        +"\no raio está á " + String.format("%.2f",distancia) + "metros de distâcia!");


    }
    public static double lightningStrikeDistance(int time){
        double distance = time * 360;
        return distance;
    }
}
