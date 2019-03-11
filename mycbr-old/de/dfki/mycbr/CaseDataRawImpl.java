/*
 * myCBR License 1.1
 *
 * Copyright (c) 2008
 * Thomas Roth-Berghofer, Armin Stahl & Deutsches Forschungszentrum f&uuml;r K&uuml;nstliche Intelligenz DFKI GmbH
 * Further contributors: myCBR Team (see http://mycbr-project.net/contact.html for further information 
 * about the myCBR Team). 
 * All rights reserved.
 *
 * myCBR is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 * Since myCBR uses some modules, you should be aware of their licenses for
 * which you should have received a copy along with this program, too.
 * 
 * endOfLic */
package de.dfki.mycbr;

import java.util.HashMap;

/**
 * Cases created using XML files first are CaseDataRawImpl objects.
 * Then they are passed to the modelprovider to build CaseInstance objects
 * 
 * @author myCBR Team
 */
public class CaseDataRawImpl extends HashMap<String, Object> implements CaseDataRaw
{
	
	private static final long serialVersionUID = 1L;
	
	private String caseName;
	private String typeName; 
	
	/**
	 * Creates a case as raw data with the specified name and type 
	 * @param caseName
	 * @param typeName
	 */
	public CaseDataRawImpl(String caseName, String typeName)
	{
		this.caseName = caseName;
		this.typeName = typeName;
	}

	/**
	 *  Gets the name of this case
	 * @return name of this case instance.
	 */
	public String getCaseName()
	{
		return caseName;
	}

	/**
	 * Returns the value of this case for the given slot.
	 * @param slotname name of a slot.
	 * @return value for the given slot ( type is Integer, Float, String,... )
	 */
	public Object getSlotValue(String slotname)
	{
		return get(slotname);
	}

	/**
	 * Sets the value of this case for the given slot.
	 * @param slotname name of a slot.
	 * @param value for the given slot ( type is Integer, Float, String,... )
	 */
	public void setSlotValue(String slotname, Object value) {
		put(slotname, value);
	}
	
	/**
	 *  Gets the type name of this case
	 * @return type name of this case instance.
	 */
	public String getTypeName()
	{
		return typeName;
	}

	/**
	 *  Sets the name of this case
	 * @param caseName the case should have this name
	 */
	public void setCaseName(String caseName) {
		this.caseName = caseName;
	}

	/**
	 *  Sets the type name of this case
	 * @param typeName the type should have this name
	 */
	public void setTypeName(String typeName) {
		this.typeName = typeName;
	}


}
