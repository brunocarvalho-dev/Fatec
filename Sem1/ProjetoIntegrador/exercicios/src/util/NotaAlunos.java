package util;

import javax.swing.*;

public class NotaAlunos {


    public float mediaExame(float media) {
        JOptionPane.showMessageDialog(null, "Sua média foi " + String.format("%.1f", media) + ","
                + "\nvocê não atingiu o mínimo de 7 pontos, portanto, será necessário realizar o exame.");
        float notaExameFinal = lerNota("Digite a nota do EXAME FINAL (entre 0 e 10): ");
        media = (media + notaExameFinal) / 2;
        return media;
    }


    public float lerNota(String mensagem) {
        boolean valid = true;
        float nota = Float.MIN_VALUE;
        while (valid) {
            try {
                nota = Float.valueOf(javax.swing.JOptionPane.showInputDialog(mensagem).replace(",", "."));
                if (nota < 0 || nota > 10) {
                    javax.swing.JOptionPane.showMessageDialog(null, "Nota inválida. Por favor, digite um valor entre 0 e 10.");
                } else {
                    valid = false;
                }
            } catch (NumberFormatException e) {
                javax.swing.JOptionPane.showMessageDialog(null, "Entrada inválida. Por favor, digite um número.");
            }
        }
        return nota;
    }

    public String aprovacao(float media) {
        String msg = "";
        if (media < 5) {
            msg = ("\nAluno(a) reprovado!!\nSua nota foi" + String.format("%.1f", media) + " não atingiu o minino de 5 pontos! :(\n");
        } else if (media < 9) {
            msg = ("\nAluno(a) aprovado!!\nSua nota foi " + String.format("%.1f", media) + ", atingiu o minino de 5 pontos.\n");
        } else {
            msg = ("\nAluno(a) Aprovado!!\nSua nota foi " + String.format("%.1f", media) + ", parabéns pelo seu desempenho!! :)\n");
        }
        return msg;
    }
}
