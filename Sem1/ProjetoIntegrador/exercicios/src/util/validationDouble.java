package util;

import javax.swing.*;

public class validationDouble {
    private double valor1;
    private boolean validation = true;


    public double getValor() {
        return valor1;
    }

    private void setValor1(double valor1) {
        this.valor1 = valor1;
    }

    public validationDouble(String msg1) {

        do{
            try{
                valor1 = Double.parseDouble(JOptionPane.showInputDialog(msg1).replace(",","."));
                validation = false;
                setValor1(valor1);
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Valor da base inválido, digite novamente");
            }
        }while (validation);


    }
}
