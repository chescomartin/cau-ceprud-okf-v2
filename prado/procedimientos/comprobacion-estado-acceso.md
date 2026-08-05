---
type: Procedure
title: Comprobación del estado de acceso
description: Procedimiento para determinar por qué una persona no puede acceder a PRADO y distinguir entre autenticación, matrícula e incidencia administrativa.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
usual_ticket_category: Acceso
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - acceso
  - autenticacion
  - idp
  - oficina-virtual
  - incidencia-administrativa
---

# Comprobación del estado de acceso

## Objetivo

Determinar por qué una persona no puede acceder a PRADO y establecer si la causa corresponde a:

- un problema de autenticación;
- una incidencia administrativa;
- una ausencia de matrícula;
- una asignación docente incorrecta;
- un retraso de actualización;
- o una situación todavía no identificada.

## Cuándo aplicar este procedimiento

Aplicar cuando una persona indique, por ejemplo:

- que no puede entrar en PRADO;
- que recibe un error al autenticarse;
- que su acceso dejó de funcionar;
- que la secretaría ya regularizó su expediente, pero PRADO sigue bloqueado;
- que puede acceder a otros servicios de la UGR, pero no a PRADO;
- que no sabe si el problema está en su matrícula o en su cuenta.

## Cuándo no aplicar este procedimiento

No utilizarlo cuando:

- la persona entra en PRADO, pero no ve una asignatura;
- el curso existe, pero está oculto;
- el problema afecta únicamente a una actividad o recurso;
- se trata de una participación suspendida o no activa ya identificada;
- existe un usuario duplicado confirmado.

## Datos que hay que solicitar

Obtener los siguientes datos:

- nombre y apellidos;
- correo electrónico institucional;
- tipo de usuario:
  - estudiante;
  - docente;
  - docente externo;
- plataforma afectada:
  - PRADO Grado;
  - PRADO Posgrado;
- curso académico;
- dirección desde la que intenta acceder;
- mensaje de error exacto;
- fecha y hora aproximada del último intento;
- confirmación de si puede entrar en otros servicios institucionales;
- captura de pantalla, cuando sea posible.

## Comprobaciones iniciales

### 1. Confirmar la plataforma

Comprobar que la persona accede a:

- PRADO Grado, cuando corresponde a estudios de Grado;
- PRADO Posgrado, cuando corresponde a másteres u otros estudios gestionados en esa plataforma;
- el curso académico correcto.

### 2. Confirmar la cuenta utilizada

Verificar:

- que utiliza la cuenta institucional adecuada;
- que el correo está correctamente escrito;
- que no está intentando acceder con una cuenta personal;
- que la cuenta corresponde a la identidad de la persona.

### 3. Comprobar el Proveedor de identidad

Revisar la información disponible en el [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md).

Comprobar:

- si la identidad aparece correctamente;
- si los atributos corresponden al curso académico vigente;
- si existe una incidencia administrativa;
- si hay alguna discrepancia entre la cuenta y los datos académicos.

### 4. Consultar el estado en Oficina Virtual

Para el alumnado, revisar la [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md).

Comprobar:

- si aparece una incidencia administrativa;
- si consta la matrícula;
- qué centro o centros son responsables;
- si el expediente ya ha sido desbloqueado.

### 5. Comprobar matrícula o asignación

Cuando no exista un bloqueo administrativo:

- para alumnado, revisar la matrícula oficial;
- para profesorado, revisar el [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md);
- utilizar las [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md) cuando sea necesario.

### 6. Comprobar los plazos de actualización

Si la secretaría o el departamento ha realizado una modificación reciente, aplicar los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md).

## Árbol de decisión

### Caso 1. Existe una incidencia administrativa

1. informar de que el expediente está bloqueado;
2. indicar el centro responsable;
3. remitir a la secretaría correspondiente;
4. no intentar retirar el bloqueo desde PRADO;
5. clasificar el ticket como [Incidencia administrativa](/prado/iris/incidencia-administrativa.md).

### Caso 2. La incidencia administrativa ya se ha retirado

1. comprobar cuándo fue retirada;
2. tener en cuenta el retraso del IdP y la caché de PRADO;
3. esperar el plazo de actualización;
4. pedir a la persona que vuelva a probar;
5. escalar si el acceso sigue bloqueado después del plazo.

### Caso 3. La matrícula no consta

1. no realizar una matrícula manual ordinaria;
2. indicar que debe revisarse en la secretaría;
3. identificar el centro responsable;
4. clasificar el ticket como `Matrícula`.

### Caso 4. El docente no consta en la asignación oficial

1. no realizar un alta manual ordinaria;
2. indicar que debe revisarse la asignación en origen;
3. aplicar el procedimiento [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md);
4. clasificar el ticket como [Ordenación docente](/prado/iris/ordenacion-docente.md).

### Caso 5. La situación administrativa y académica es correcta

1. revisar el IdP;
2. comprobar el mensaje de error;
3. descartar una cuenta incorrecta o duplicada;
4. revisar si el problema afecta únicamente a la autenticación;
5. clasificar el ticket como [Acceso](/prado/iris/acceso.md).

### Caso 6. No se determina la causa

1. registrar todas las comprobaciones realizadas;
2. solicitar los datos que falten;
3. escalar cuando proceda;
4. clasificar provisionalmente como `Sin resolver`.

## Particularidad de Posgrado

La Consulta de Estado para Acceso a PRADO en Oficina Virtual no debe utilizarse como única referencia para comprobar la matrícula de Posgrado.

En estos casos, debe comprobarse la información mediante las vistas de bases de datos.

## Resultado esperado

Al finalizar la comprobación debe quedar identificado:

- si la persona puede autenticarse;
- si existe una incidencia administrativa;
- si consta la matrícula o asignación oficial;
- si el problema es un retraso de actualización;
- qué unidad debe actuar;
- y qué categoría de IRIS corresponde.

## Plantillas de respuesta

### Plantilla 1. Solicitud de información

Estimada/o [nombre]:

Para revisar el problema de acceso a PRADO necesitamos que nos facilite:

- el correo institucional con el que intenta acceder;
- la plataforma afectada: PRADO Grado o PRADO Posgrado;
- el mensaje de error exacto;
- la fecha y hora aproximada del último intento;
- y una captura de pantalla, cuando sea posible.

También debe comprobar en su Oficina Virtual el apartado **«Consulta de Estado para Acceso a PRADO»**.

Un saludo.

---

### Plantilla 2. Incidencia administrativa

Estimada/o [nombre]:

Hemos comprobado que existe una incidencia administrativa asociada a su expediente.

Debe contactar con la secretaría del centro que aparece en el apartado **«Consulta de Estado para Acceso a PRADO»** de su Oficina Virtual.

Desde el CEPRUD no podemos retirar este bloqueo administrativo.

Un saludo.

---

### Plantilla 3. Acceso correcto en origen

Estimada/o [nombre]:

La matrícula o asignación oficial y la situación administrativa constan correctamente.

Vamos a revisar el problema como una incidencia de autenticación o acceso a PRADO.

Para continuar necesitamos el mensaje de error exacto y una captura de pantalla del intento de acceso.

Un saludo.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)

## Categorías de IRIS relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Sin resolver](/prado/iris/sin-resolver.md)

## Procedimientos relacionados

- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Acceso de un docente externo](/prado/procedimientos/acceso-docente-externo.md)
