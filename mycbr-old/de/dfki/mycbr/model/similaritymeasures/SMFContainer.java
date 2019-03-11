/**
 MyCBR License 1.1

 Copyright (c) 2008
 Thomas Roth-Berghofer, Armin Stahl & Deutsches Forschungszentrum f&uuml;r K&uuml;nstliche Intelligenz DFKI GmbH
 Further contributors: myCBR Team (see http://mycbr-project.net/contact.html for further information 
 about the mycbr Team). 
 All rights reserved.

 MyCBR is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

 Since MyCBR uses some modules, you should be aware of their licenses for
 which you should have received a copy along with this program, too.
 
 endOfLic**/
package de.dfki.mycbr.model.similaritymeasures;

import java.util.HashMap;

import de.dfki.mycbr.model.vocabulary.ModelInstance;


/**
 * @author myCBR Team
 *
 */
public class SMFContainer extends HashMap<String, SMFHolder> {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private static SMFContainer instance = new SMFContainer();
	
	private SMFContainer() {}
	
	public static SMFContainer getInstance() {
		return instance;
	}
	
	public static SMFContainer initInstance() {
		instance = new SMFContainer();	
		return instance;
	}
	
	public static void resetInstance() {
		instance = null;
	}
	
	/**
	 * returns the smfunction holder for the given instance. if there doesnt
	 * exist a holder for this inst yet, a new one will be created.
	 * 
	 * @param inst
	 * @return SMFHolder all similarity functions defined for this model
	 *         instance (slot/cls) or null if inst==null.
	 */
	public SMFHolder getSMFHolderForModelInstance(ModelInstance inst) {
		if (inst == null)
			return null;

		String key = inst.getName();
		SMFHolder holder = get(key);
		if (holder == null) {
			holder = new SMFHolder(inst);
			put(key, holder);
		}
		return holder;
	}

}
