---
type: Rule
title: Bajas automáticas y calendario de ejecución
description: Regla sobre la aplicación automática de bajas en PRADO a partir de las bases de datos oficiales.
service: PRADO
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
source_schedule_reviewed: 2025-11-25
tags:
  - prado
  - bajas-automaticas
  - participacion-suspendida
  - sincronizacion
  - matricula
  - asignacion-docente
---

# Bajas automáticas y calendario de ejecución

## Definición

Las bajas automáticas son procesos mediante los que PRADO actualiza o suspende participaciones cuando una persona deja de constar en las bases de datos oficiales de matrícula o asignación docente.

Pueden afectar a:

- alumnado que se da de baja de una asignatura;
- alumnado que cambia oficialmente de grupo;
- profesorado que deja de tener asignada docencia;
- participaciones que ya no deben mantenerse activas en un espacio.

## Fuente de la baja

La baja debe proceder de una modificación registrada en el sistema oficial correspondiente:

- matrícula del alumnado;
- asignación docente del profesorado;
- otra fuente institucional utilizada por los automatismos de PRADO.

PRADO no genera una baja oficial por una simple petición realizada en un ticket.

## Calendario interno de ejecución

La documentación interna recoge el siguiente calendario, revisado el **25 de noviembre de 2025**:

- PRADO Grado: martes y viernes;
- PRADO Posgrado: lunes y jueves.

Este calendario debe revisarse periódicamente, ya que puede cambiar.

## Efecto habitual

Cuando una persona deja de llegar desde la fuente oficial, su participación puede quedar como:

- [participación suspendida](../usuarios-y-roles/participacion-suspendida.md).

En ese estado:

- no puede acceder al espacio;
- no recibe notificaciones;
- continúa apareciendo temporalmente en la relación de participantes;
- el profesorado puede eliminar la participación cuando proceda.

## Diferencia entre alta, baja y sincronización

### Alta

La persona comienza a llegar desde una fuente oficial y PRADO genera su participación.

### Baja

La persona deja de llegar desde la fuente oficial y PRADO suspende o elimina la participación según el proceso aplicable.

### Sincronización

Es el proceso de intercambio y actualización que hace que el cambio registrado en origen se refleje en PRADO.

Una baja puede constar oficialmente antes de que se ejecute el siguiente proceso automático.

## Comprobaciones del CAU

Ante una consulta sobre una baja pendiente, comprobar:

1. la identidad y el correo institucional;
2. la plataforma:
   - PRADO Grado;
   - PRADO Posgrado;
3. el curso académico;
4. la asignatura y el grupo;
5. si afecta a alumnado o profesorado;
6. si la baja consta en la fuente oficial;
7. la fecha del cambio;
8. las [vistas de bases de datos](vistas-bases-datos.md);
9. el calendario de ejecución;
10. el estado actual de la participación;
11. si existe una participación activa en otro grupo o espacio;
12. si ya ha transcurrido el siguiente proceso previsto.

## Árbol de decisión

### La baja no consta en la fuente oficial

No se trata todavía de una baja automática pendiente.

Actuación:

- remitir a la unidad responsable del dato;
- no modificar manualmente la participación;
- clasificar según el origen:
  - `Matrícula`;
  - `Ordenación docente`.

### La baja consta y todavía no ha llegado el día de ejecución

Actuación:

- informar de que la actualización no es inmediata;
- esperar el siguiente proceso previsto;
- no reactivar ni eliminar manualmente la participación salvo procedimiento específico.

Categoría de IRIS:

- [Baja de usuario](../iris/baja-usuario.md).

### La baja consta y ya ha pasado el día de ejecución

Actuación:

1. volver a comprobar las vistas;
2. confirmar que la información sigue siendo correcta;
3. revisar el estado de la participación;
4. escalar si el automatismo no ha aplicado la baja.

### Existe un cambio de grupo

Actuación:

1. comprobar el grupo oficial actual;
2. confirmar el alta en el grupo nuevo;
3. comprobar la baja o suspensión en el grupo anterior;
4. no reactivar el grupo anterior si la modificación es correcta.

## Qué no debe hacerse

No debe:

- reactivarse una participación suspendida sin comprobar la fuente oficial;
- eliminarse manualmente una participación para simular una baja que no consta;
- realizarse una matrícula manual para contrarrestar una baja oficial;
- prometer que la baja se reflejará de forma inmediata;
- confundirse una participación suspendida con una participación no activa;
- utilizarse `Acceso` cuando la causa real es una baja oficial.

## Resultado esperado

Al finalizar la revisión debe quedar identificado:

- si la baja consta en origen;
- cuándo se registró;
- qué proceso automático debe aplicarla;
- si ya ha transcurrido el siguiente día de ejecución;
- si la participación está activa, suspendida o eliminada;
- qué categoría de IRIS corresponde;
- y si debe escalarse la incidencia.

## Plantillas de respuesta

### Plantilla 1. Baja pendiente

Estimada/o [nombre]:

La baja ya consta en la información oficial, pero su reflejo en PRADO depende del siguiente proceso automático de actualización.

Las bajas no se aplican de forma inmediata. Revisaremos el resultado después de la próxima ejecución prevista.

Un saludo.

---

### Plantilla 2. Baja no registrada

Estimada/o [nombre]:

La baja indicada todavía no consta en la información oficial que recibe PRADO.

Debe solicitar la modificación a [secretaría/departamento/unidad responsable]. Cuando quede registrada en origen, PRADO la procesará mediante sus automatismos.

Un saludo.

---

### Plantilla 3. Baja no aplicada tras el calendario

Estimada/o [nombre]:

La baja consta correctamente en la fuente oficial y ya ha transcurrido el proceso de actualización previsto.

Vamos a revisar por qué el automatismo no la ha aplicado todavía.

Un saludo.

## Categorías de IRIS relacionadas

- [Baja de usuario](../iris/baja-usuario.md)
- [Matrícula](../iris/matricula.md)
- [Ordenación docente](../iris/ordenacion-docente.md)
- [Gestión manual](../iris/gestion-manual.md)
- Sin resolver

## Conceptos relacionados

- [Vistas de bases de datos](vistas-bases-datos.md)
- [Plazos de sincronización y actualización](plazos-sincronizacion.md)
- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)
- [Matrícula manual](matricula-manual.md)
- [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md)
- [Participación suspendida](../usuarios-y-roles/participacion-suspendida.md)
- [Participación no activa](../usuarios-y-roles/participacion-no-activa.md)
