---
type: UserState
title: Participación suspendida
description: Estado de una participación en PRADO cuando la persona deja de llegar desde las bases de datos oficiales.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - usuarios
  - participacion
  - suspendido
  - bajas-automaticas
  - matricula
---

# Participación suspendida

## Definición

Una participación queda **suspendida** cuando la persona deja de llegar a PRADO desde las bases de datos oficiales.

Puede afectar a:

- alumnado que deja de constar en la matrícula oficial;
- profesorado que deja de constar en la asignación docente;
- una asignatura completa;
- un grupo concreto.

La persona continúa apareciendo en la relación de participantes, pero su acceso al espacio queda desactivado.

## Efectos

Cuando una participación está suspendida:

- la persona no puede acceder al espacio docente;
- no recibe notificaciones de ese espacio;
- el profesorado puede eliminar la participación si lo considera necesario;
- la actividad previa puede seguir asociada a la participación mientras no se elimine.

## Causas habituales

La suspensión puede producirse cuando:

- se tramita una baja de matrícula;
- se modifica el grupo oficial;
- se elimina una asignación docente;
- la persona deja de aparecer en las vistas de bases de datos;
- actúan los procesos automáticos de actualización de PRADO.

## Diferencia con «No activo»

### Participación suspendida

La persona estuvo vinculada mediante una fuente oficial, pero deja de llegar desde esa fuente.

Ejemplos:

- un estudiante se da de baja de la asignatura;
- un estudiante cambia oficialmente de grupo;
- un docente deja de tener asignada la docencia.

### Participación no activa

La persona fue incorporada manualmente al margen de la matrícula oficial y los automatismos detectan que no consta como participante oficial.

No deben considerarse estados equivalentes.

## Comprobaciones del CAU

Ante una consulta sobre una participación suspendida, comprobar:

1. la identidad y el correo institucional de la persona;
2. la plataforma y el curso académico;
3. la asignatura y el grupo afectados;
4. si la persona aparece como suspendida en Participantes;
5. si consta actualmente en la matrícula o asignación oficial;
6. si ha habido una modificación reciente;
7. las [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md);
8. los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md);
9. si la suspensión afecta solo a un espacio o a varios;
10. si existe una participación activa duplicada en otro grupo o espacio.

## Árbol de decisión

### Caso 1. La baja oficial es correcta

1. confirmar que la persona ya no consta en la fuente oficial;
2. explicar que la suspensión refleja esa baja;
3. no reactivar manualmente la participación;
4. clasificar según la causa:
   - `Baja de usuario`;
   - `Matrícula`;
   - [Ordenación docente](/prado/iris/ordenacion-docente.md).

### Caso 2. La persona sigue constando oficialmente

1. comprobar cuándo se registró la información;
2. revisar las vistas de bases de datos;
3. aplicar los plazos de actualización;
4. escalar si la participación continúa suspendida después del plazo.

### Caso 3. El estudiante ha cambiado de grupo

1. comprobar el grupo oficial actual;
2. confirmar si existe ya una participación activa en el nuevo grupo;
3. no reactivar el grupo anterior si la baja es correcta;
4. esperar o revisar la actualización automática cuando el cambio sea reciente.

### Caso 4. El docente ha perdido la asignación

1. revisar el [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md);
2. comprobar si la baja o modificación es correcta;
3. no realizar un alta manual ordinaria;
4. aplicar [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md).

### Caso 5. La participación puede eliminarse

El profesorado puede eliminar una participación suspendida cuando ya no sea necesaria.

Antes de hacerlo, debe tenerse en cuenta que la eliminación puede afectar a la consulta posterior de la actividad vinculada a esa participación.

## Qué no debe hacerse

No debe:

- reactivarse manualmente una participación sin comprobar la fuente oficial;
- utilizarse una matrícula manual para sustituir una matrícula oficial ausente;
- confundirse una participación suspendida con una incidencia de autenticación general;
- clasificarse automáticamente como `Acceso`;
- eliminarse sin valorar la actividad previa asociada.

## Resultado esperado

Al finalizar la revisión debe quedar identificado:

- por qué se ha suspendido la participación;
- si la baja oficial es correcta;
- si existe una actualización pendiente;
- si la persona tiene una participación activa alternativa;
- qué unidad debe corregir los datos cuando exista un error;
- y qué categoría de IRIS corresponde.

## Plantillas de respuesta

### Plantilla 1. Baja oficial correcta

Estimada/o [nombre]:

La participación aparece suspendida porque ya no consta activa en la información oficial de matrícula o asignación docente.

Este estado impide el acceso al espacio y el envío de notificaciones.

Para aclarar o modificar la situación oficial debe contactar con [secretaría/departamento].

Un saludo.

---

### Plantilla 2. Modificación reciente

Estimada/o [nombre]:

La modificación oficial se ha realizado recientemente y su reflejo en PRADO puede no ser inmediato.

Vamos a comprobar la actualización de los datos. Mientras tanto, no es recomendable realizar un alta manual, ya que podría entrar en conflicto con los automatismos de la plataforma.

Un saludo.

---

### Plantilla 3. Cambio de grupo

Estimada/o [nombre]:

La participación del grupo anterior aparece suspendida porque su matrícula oficial ha cambiado.

Compruebe en PRADO si ya dispone de acceso al nuevo grupo. La participación anterior no debe reactivarse cuando la baja oficial es correcta.

Un saludo.

## Categorías de IRIS relacionadas

- [Baja de usuario](/prado/iris/baja-usuario.md)
- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Sin resolver](/prado/iris/sin-resolver.md)

## Conceptos relacionados

- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)

## Procedimientos relacionados

- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
