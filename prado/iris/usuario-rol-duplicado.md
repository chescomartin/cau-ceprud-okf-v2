---
type: TicketCategory
title: Usuario/rol duplicado
description: Tema de ayuda para incidencias en las que una misma persona aparece con dos perfiles, dos identificaciones o una combinación de roles que provoca problemas en PRADO.
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
  - E-CAMPUS
  - ABIERTA UGR
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - iris
  - usuario-duplicado
  - rol-duplicado
  - identificacion
  - pasaporte
  - nie
  - perfiles
---

# Usuario/rol duplicado

## Definición

Utilizar esta categoría cuando la incidencia está relacionada con:

- una misma persona que aparece con dos perfiles;
- dos números de identificación diferentes asociados a la misma persona;
- un cambio de documento identificativo, por ejemplo de pasaporte a NIE;
- una misma persona con doble rol cuando esa situación le provoca problemas;
- actividad académica o participaciones repartidas entre dos perfiles;
- un fallo en el proceso automático de unificación o migración de la cuenta.

## Cuándo utilizar esta categoría

Utilizar `Usuario/rol duplicado` cuando:

- la persona aparece dos veces en PRADO;
- existe un perfil antiguo y otro nuevo;
- la matrícula está asociada al perfil nuevo, pero la actividad anterior permanece en el antiguo;
- el correo institucional está asociado a un perfil distinto del que contiene la actividad;
- se ha producido un cambio de número de identificación;
- la persona tiene una combinación de roles que provoca un funcionamiento incorrecto;
- el automatismo de migración no ha completado correctamente el cambio.

## Cuándo no utilizar esta categoría

No utilizar `Usuario/rol duplicado` cuando:

- la persona tiene dos roles legítimos y no existe ningún problema;
- falta una matrícula oficial;
- falta una asignación docente;
- la participación está suspendida;
- la participación está no activa;
- el problema es únicamente de autenticación;
- existe una incidencia administrativa;
- el curso está oculto.

## Funcionamiento habitual del automatismo

Cuando se registra un cambio de número de identificación, PRADO dispone de un automatismo destinado a detectar ambos perfiles.

El resultado esperado es:

1. identificar el perfil anterior y el perfil nuevo;
2. conservar como principal el perfil asociado al nuevo número de identificación;
3. asociar correctamente la matrícula y el correo institucional al perfil nuevo;
4. trasladar al perfil nuevo la actividad desarrollada con el perfil anterior;
5. modificar el correo del perfil anterior para señalar que se trata de una cuenta duplicada.

## Plazo específico

La documentación interna establece para este cambio un plazo de hasta **48 horas** desde que la modificación se hace efectiva en la secretaría.

Este plazo es específico para el cambio de identificación y no debe confundirse con el plazo general de 24 horas utilizado en otras sincronizaciones.

## Datos que deben solicitarse

Solicitar:

- nombre y apellidos;
- correo institucional;
- plataforma afectada;
- curso académico;
- identificación anterior;
- identificación actual;
- tipo de cambio realizado;
- fecha en que la secretaría registró el cambio;
- asignaturas o espacios afectados;
- descripción de la actividad que aparece en cada perfil;
- capturas de pantalla, cuando sea posible.

Los datos identificativos deben tratarse únicamente mediante los canales y procedimientos institucionales autorizados.

## Comprobaciones previas

Antes de clasificar el ticket:

1. confirmar que ambos perfiles corresponden a la misma persona;
2. comprobar el correo institucional asociado a cada perfil;
3. identificar el número de identificación anterior y el actual;
4. comprobar cuál de los perfiles recibe actualmente la matrícula o asignación oficial;
5. revisar en qué perfil se conserva la actividad anterior;
6. comprobar cuándo se registró el cambio en la secretaría;
7. verificar si han transcurrido 48 horas;
8. revisar si el automatismo ha marcado el perfil antiguo como duplicado;
9. comprobar si existe además un problema de roles;
10. evitar cualquier modificación manual hasta identificar claramente ambos perfiles.

## Árbol de decisión

### El cambio se registró hace menos de 48 horas

Actuación:

1. informar de que la actualización no es inmediata;
2. esperar hasta que transcurran 48 horas desde el registro efectivo;
3. volver a comprobar ambos perfiles;
4. no realizar cambios manuales prematuros.

Categoría:

- `Usuario/rol duplicado`.

### Han transcurrido más de 48 horas y la unificación es correcta

Comprobar que:

- el perfil nuevo contiene la matrícula actual;
- el correo institucional está correctamente asociado;
- la actividad anterior se ha trasladado;
- el perfil antiguo aparece identificado como duplicado.

Cuando todo sea correcto, informar a la persona y cerrar el ticket.

### Han transcurrido más de 48 horas y el automatismo ha fallado

Actuación:

1. documentar claramente ambos perfiles;
2. registrar la identificación anterior y la nueva;
3. indicar dónde se encuentra la matrícula;
4. indicar dónde se conserva la actividad;
5. escalar para la revisión técnica del proceso de unificación;
6. no improvisar cambios manuales sin seguir el procedimiento interno.

Categoría:

- `Usuario/rol duplicado`.

### Existe un doble rol sin duplicidad de perfil

Comprobar si:

- los dos roles son legítimos;
- el problema afecta a la visualización, los permisos o el acceso;
- existen realmente dos cuentas o solo una cuenta con varios roles.

Utilizar esta categoría únicamente cuando la combinación de roles sea la causa comprobada del problema.

### La causa es otra

Clasificar según corresponda:

- [Matrícula](matricula.md): falta o es incorrecta la matrícula oficial;
- [Ordenación docente](ordenacion-docente.md): falta o es incorrecta la asignación docente;
- [Acceso](acceso.md): no puede autenticarse y no existe duplicidad;
- [Incidencia administrativa](incidencia-administrativa.md): existe un bloqueo administrativo;
- [Gestión manual](gestion-manual.md): la duplicidad procede de una actuación manual;
- `Sin resolver`: no puede determinarse la causa.

## Qué no debe hacerse

No debe:

- eliminarse uno de los perfiles sin comprobar dónde está la actividad;
- cambiarse el correo institucional de forma improvisada;
- trasladarse manualmente información sin seguir el procedimiento técnico;
- considerarse duplicidad cualquier caso con varios roles;
- pedirse a la persona que utilice indistintamente ambos perfiles;
- cerrarse el ticket antes de comprobar el resultado después de las 48 horas;
- incluirse documentación identificativa sensible en campos o canales no autorizados.

## Resultado esperado

Al finalizar la revisión debe quedar identificado:

- si existen realmente dos perfiles;
- qué identificación corresponde a cada uno;
- cuál es el perfil principal;
- dónde está asociada la matrícula o asignación;
- dónde se encuentra la actividad anterior;
- si ha actuado correctamente el automatismo;
- si debe esperarse el plazo de 48 horas;
- si procede una intervención técnica;
- y qué categoría de IRIS corresponde.

## Plantillas de respuesta

### Plantilla 1. Cambio dentro del plazo de 48 horas

Estimada/o [nombre]:

El cambio de su número de identificación se ha registrado recientemente. La actualización y unificación de los perfiles en PRADO puede necesitar hasta 48 horas desde que el cambio se hace efectivo en la secretaría.

Le recomendamos que vuelva a comprobarlo una vez transcurrido ese plazo.

Un saludo.

---

### Plantilla 2. Revisión técnica necesaria

Estimada/o [nombre]:

Hemos comprobado que existen dos perfiles asociados a sus datos y que el proceso automático de unificación no se ha completado correctamente después del plazo previsto.

Vamos a trasladar la incidencia para que se revise la asociación de la matrícula, el correo institucional y la actividad desarrollada.

Un saludo.

---

### Plantilla 3. La unificación se ha completado

Estimada/o [nombre]:

El cambio de identificación ya se ha procesado correctamente. Su matrícula, correo institucional y actividad se encuentran asociados al perfil actualizado.

Debe acceder con su cuenta institucional habitual.

Un saludo.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](../conceptos-y-reglas/proveedor-identidad-idp.md)
- [Vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)
- [Altas automáticas desde bases de datos oficiales](../conceptos-y-reglas/altas-automaticas.md)

## Estados relacionados

- [Participación suspendida](../usuarios-y-roles/participacion-suspendida.md)
- [Participación no activa](../usuarios-y-roles/participacion-no-activa.md)

## Categorías relacionadas

- [Acceso](acceso.md)
- [Matrícula](matricula.md)
- [Ordenación docente](ordenacion-docente.md)
- [Gestión manual](gestion-manual.md)
- [Incidencia administrativa](incidencia-administrativa.md)
- Sin resolver
