---
type: Rule
title: Matrícula manual
description: Regla sobre la incorporación manual de participantes a espacios de PRADO al margen de las bases de datos oficiales.
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
  - matricula-manual
  - gestion-manual
  - alumnado
  - automatismos
  - no-activo
---

# Matrícula manual

## Definición

La matrícula manual es la incorporación de una persona a un espacio de PRADO realizada directamente por un usuario con permisos, al margen de las bases de datos oficiales de matrícula o asignación docente.

Puede afectar a:

- alumnado incorporado con rol de estudiante;
- profesorado incorporado manualmente en situaciones excepcionales;
- personas añadidas a espacios de pruebas, gestión o formación.

## Regla general

La matrícula manual no debe utilizarse como solución ordinaria para sustituir:

- una matrícula oficial que todavía no consta;
- una asignación docente pendiente;
- una asimilación docente no registrada;
- un cambio de grupo pendiente de actualización;
- una baja o alta que debe llegar desde las bases de datos oficiales.

Las altas deben producirse preferentemente mediante los automatismos alimentados por las fuentes institucionales.

## Riesgos

Una matrícula manual puede provocar:

- que la persona quede marcada posteriormente como [participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md);
- pérdida de acceso al espacio;
- falta de notificaciones;
- discrepancias entre PRADO y la matrícula oficial;
- duplicidad de participaciones;
- problemas cuando actúan las altas y bajas automáticas;
- dificultad para identificar la causa real de una incidencia.

## Responsabilidad

Cuando el profesorado incorpora manualmente a una persona con rol de estudiante, esa actuación queda bajo su responsabilidad.

No debe recomendarse esta posibilidad como respuesta habitual del CAU.

## Actuaciones manuales excepcionales

El personal técnico puede realizar altas manuales de docentes únicamente en situaciones justificadas, por ejemplo:

- docentes con créditos prácticos sin grupo oficial asignado;
- autorización expresa del Servicio de Ordenación Académica;
- docentes próximos que necesitan un Espacio Docente de Pruebas Personal;
- otros casos expresamente contemplados en un procedimiento interno.

La autorización debe quedar registrada en el ticket cuando sea necesaria.

## Casos en los que no procede

### Falta la matrícula oficial de un estudiante

No debe incorporarse manualmente.

Debe remitirse a la secretaría correspondiente para corregir la matrícula en origen.

### Existe una asimilación pendiente

No debe simularse la unificación mediante matrículas manuales.

Debe aplicarse:

- [Tramitación de una asimilación docente](/prado/procedimientos/tramitacion-asimilacion-docente.md).

### Cambio de grupo reciente

Debe comprobarse la matrícula oficial y esperar la actualización automática.

### Docente de teoría ausente del POD

Debe corregirse la asignación en el [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md).

### Docente con créditos prácticos y grupo SG

Puede requerir una actuación manual excepcional según el procedimiento:

- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md).

## Comprobaciones del CAU

Antes de realizar o recomendar cualquier alta manual, comprobar:

1. la identidad y el correo institucional;
2. la plataforma y el curso académico;
3. el espacio docente;
4. el rol solicitado;
5. la matrícula o asignación oficial;
6. las [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md);
7. los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md);
8. si existe una asimilación;
9. si la persona ya aparece con otra participación;
10. si existe autorización expresa para la actuación manual.

## Árbol de decisión

### La persona debe llegar desde una fuente oficial

- no realizar el alta manual;
- corregir los datos en origen;
- esperar la sincronización;
- clasificar el ticket según la causa.

### Existe una excepción documentada

- aplicar el procedimiento específico;
- conservar la autorización en el ticket;
- registrar la actuación;
- comprobar posteriormente el resultado.

### No se puede determinar la procedencia del alta

- no actuar todavía;
- solicitar los datos que falten;
- escalar o clasificar como `Sin resolver`.

## Resultado esperado

La gestión debe asegurar que:

- las participaciones ordinarias proceden de fuentes oficiales;
- las actuaciones manuales son excepcionales y trazables;
- no se crean duplicidades;
- no se sustituye una corrección administrativa o académica;
- la categoría de IRIS refleja la causa real.

## Plantilla de respuesta

Estimada/o [nombre]:

PRADO se actualiza a partir de la información oficial de matrícula y asignación docente.

No es recomendable realizar una incorporación manual para sustituir una matrícula o asignación que todavía no consta, ya que los automatismos pueden marcar posteriormente esa participación como no activa.

Debe solicitar la corrección de los datos a [secretaría/departamento/unidad responsable]. Cuando la información oficial se actualice, el alta se reflejará automáticamente en PRADO.

Un saludo.

## Categorías de IRIS relacionadas

- [Gestión manual](/prado/iris/gestion-manual.md)
- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md)
- [Sin resolver](/prado/iris/sin-resolver.md)

## Conceptos relacionados

- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md)
- [Grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)
- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)

## Procedimientos relacionados

- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)
- [Alta manual de un docente con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md)
- [Tramitación de una asimilación docente](/prado/procedimientos/tramitacion-asimilacion-docente.md)
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
