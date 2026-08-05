---
type: Concept
title: Usuario duplicado o cambio de número de identificación
description: Definición y tratamiento documentado de las cuentas duplicadas originadas por un cambio de documento identificativo en PRADO.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-09-05
last_reviewed: 2026-08-03
tags:
  - prado
  - usuarios
  - duplicados
  - identificacion
  - automatismos
---

# Usuario duplicado o cambio de número de identificación

## Definición

Puede producirse una duplicación de usuario cuando una persona cambia su número de identificación, por ejemplo:

- de pasaporte a NIE;
- o de un documento identificativo anterior a otro nuevo.

Como consecuencia, PRADO puede recibir un nuevo registro para la misma persona.

## Automatismo de resolución

La documentación interna indica que existe un automatismo que detecta estos cambios.

Cuando funciona correctamente:

1. modifica el correo del usuario anterior mediante un valor con el prefijo `duplicado_`;
2. conserva como usuario principal el registro asociado al nuevo número de identificación;
3. traslada al nuevo usuario la actividad desarrollada con el perfil anterior;
4. mantiene el nuevo perfil correctamente vinculado con su matrícula y su correo institucional.

## Plazo de actualización

El plazo aplicable a este cambio se consulta en
[Parámetros operativos de PRADO](/prado/parametros-operativos.md). Es un plazo **específico**
y no debe informarse del plazo general de sincronización.

## Comprobaciones habituales

Ante una incidencia por posible duplicación, comprobar:

1. la identidad de la persona;
2. el número de identificación anterior;
3. el número de identificación actual;
4. las cuentas de correo asociadas;
5. los perfiles existentes en PRADO;
6. cuál está vinculado con la matrícula;
7. cuál está vinculado con la asignación docente;
8. la fecha en que el cambio se registró en secretaría;
9. si han transcurrido 48 horas;
10. si la actividad aparece en el perfil correcto.

## Casos frecuentes

### El cambio todavía no se refleja

Comprobar la fecha efectiva del cambio en la secretaría.

Cuando todavía no han transcurrido 48 horas, debe esperarse a que finalice el proceso automático.

### La persona aparece dos veces

Comprobar:

- los números de identificación;
- los correos;
- las matrículas;
- las asignaciones docentes;
- y qué perfil contiene la actividad previa.

Clasificación habitual:

- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)

### El automatismo ha fallado

La documentación interna indica que el fallo es poco frecuente.

Cuando ocurre, puede ser necesaria una intervención técnica manual para intercambiar y corregir los datos de ambos perfiles.

Esta actuación debe realizarse únicamente por personal técnico autorizado y dejarse documentada.

### Después de la corrección sigue sin funcionar

Comprobar:

- que se han guardado correctamente los cambios;
- que el perfil nuevo tiene el identificador y correo correctos;
- que el perfil anterior utiliza el correo ficticio con prefijo `duplicado_`;
- y que ha transcurrido el plazo indicado.

## Información que debe registrarse

Anotar:

- nombre de la persona;
- número identificativo anterior;
- número identificativo nuevo;
- correos asociados;
- perfiles afectados;
- matrícula o asignación vinculada a cada perfil;
- fecha del cambio en secretaría;
- resultado del automatismo;
- actividad trasladada;
- actuación manual realizada, cuando proceda;
- fecha de comprobación final.

## Conceptos relacionados

- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)

## Perfiles relacionados

- [Alumno oficial](/prado/usuarios-y-roles/alumno-oficial.md)
- [Docente oficial de teoría](/prado/usuarios-y-roles/docente-oficial-teoria.md)
- [Usuario con perfil docente y alumno](/prado/usuarios-y-roles/usuario-docente-alumno.md)

## Categoría de IRIS relacionada

- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)
